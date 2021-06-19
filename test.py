#import dependanceis

import discord

#define variables

client = discord.Client()


#print login message
@client.event
async def on_ready():
    print('We have logged in as {0.user}' .format(client))

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
            
client.run('ODU1OTE5OTkwMjA5NTExNDQ0.YM5fmw.9tONWdIdcg_g7XgnNZyFjrSw2No')