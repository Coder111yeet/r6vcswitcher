#import dependanceis

import discord

#define variables

client = discord.Client()
game = discord.Game("with nutz")


#print login message and set presence
@client.event
async def on_ready():
    print('We have logged in as {0.user}' .format(client))
    await client.change_presence(status=discord.Status.idle, activity=game)
    print('Set Own Rich Presence')
#commands

@client.event
async def on_message(message):
        if message.author == client.user:
            return
            
        if message.content.startswith('$hello'):
            await message.channel.send('Hello!')
            print('Sent Hello Message')
            
        if message.content.startswith('no u'):
            await message.channel.send('no u')
            print('Sent "No U Message')
            
        if message.content.startswith('nou'):
            await message.channel.send('no u')
            print('Sent "No U Message')

        if message.content.startswith('No u'):
            await message.channel.send('no u')
            print('Sent "No U Message')
            
        if message.content.startswith('Nou'):
            await message.channel.send('no u')
            print('Sent "No U Message')

#run client
            
client.run('ODU1OTE5OTkwMjA5NTExNDQ0.YM5fmw.sC-5T8IcoTsnJIbb1SeW9xB_Ar4')