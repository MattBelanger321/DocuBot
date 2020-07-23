import discord

client = discord.Client()

@client.event
async def on_message(message):
    if message.content.startswith('!test'):
        await message.channel.send('I\'m Alive MotherFucker')
    elif message.content.startswith('!help'):
        await message.channel.send('1: !help\n2: !test\nAnd that\'s all you get')

@client.event
async def on_ready():
    print(client.user.name)

client.run('NzM1NzcxNDI5MzY2MjY3OTM0.XxlMuQ.rRaqr4fXIAvlPLFudFNX7_WL2dE')
