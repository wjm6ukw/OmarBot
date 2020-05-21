import discord
import random


client=discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

    if 'omar' in message.content:
        emoji = client.get_emoji(456653084064481283)
        await message.add_reaction(emoji)
        
    if message.author.id ==  84056200450150400:         #User ID here
        if random.randint(0,10) == 10:
            emoji = client.get_emoji(456653084064481283)    #emoji id here
            await message.add_reaction(emoji)

client.run('NjY0MjQwMDE1MDkzNjYxNzE4.Xp1D4g.jzyNX2S3VuQ8EKaHsrA5ym5z7P8')