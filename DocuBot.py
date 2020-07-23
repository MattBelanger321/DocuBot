import discord
from pip._vendor import requests

client = discord.Client()


@client.event
async def on_message(message):
    if message.content.startswith('!test'):
        await message.channel.send('I\'m Alive MotherFucker')
    elif message.content.startswith('!help'):
        await message.channel.send('1: !help\n2: !test\nAnd that\'s all you get')
    elif message.content.startswith('!CDOCS'):
        x = message.content.split()  # arg array

        if len(x) != 2:
            await message.channel.send('USAGE: !CDOCS <function name>')
            return;

        URL = 'https://www.tutorialspoint.com/c_standard_library/c_function_' + x[1] + '.htm'
        # Shoutout to tutorials point

        r = requests.get(URL)

        if r.status_code != 404:
            await message.channel.send(URL)
        else:
            await message.channel.send('ERROR 404: NO DOCS FOUND')


@client.event
async def on_ready():
    print(client.user.name)


file = open('config.txt')
client.run(file.read())
