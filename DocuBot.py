import discord
from pip._vendor import requests

client = discord.Client()
special = '!'


@client.event
async def on_message(message):
    if message.author.bot:
        return

    if message.content.startswith(special + 'test'):
        await message.channel.send('I\'m Alive MotherFucker')
        return
    elif message.content.startswith(special + 'help'):
        await message.channel.send(
            'AVAILABLE COMMANDS: '+
            '1:' + special + 'help\n' +
            '2:' + special + 'test\n' +
            '3:' + special + 'CDOCS <function name>\n' +
            '4:' + special + 'ME\n' +
            'And that\'s all you get'
        )
    elif message.content.startswith(special + 'CDOCS'):
        x = message.content.split()  # arg array

        if len(x) != 2:
            await message.channel.send('USAGE: ' + special + 'CDOCS <function name>')
            return

        if await printURL('https://man7.org/linux/man-pages/man2/' + x[1] + '.2.html', message) != 0:
            return
        elif await printURL('https://man7.org/linux/man-pages/man3/' + x[1] + '.3.html', message) != 0:
            return
        else:
            await message.channel.send('ERROR 404: NO DOCS FOUND')
            return

    elif message.content.startswith(special + 'ME'):
        await message.channel.send('https://github.com/MattBelanger321/DocuBot')
        return


@client.event
async def on_ready():
    print(client.user.name)


async def printURL(URL, message) -> int:
    r = requests.get(URL)
    if r.status_code != 404:
        await message.channel.send(URL)
        return 1
    else:
        return 0


file = open('config.txt')
client.run(file.read())
