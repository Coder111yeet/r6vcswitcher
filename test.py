#import dependanceis

import discord
from discord.ext.commands import Bot
from discord import Member
#define variables

client = discord.Client()
game = discord.Game("with nutz")
bot = Bot('!')
membergame = None

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


#query member status
for activity in member.activities:
    if isinstance(activity, discord.Game):
        game = activity
        
if game is None:
    return await ctx.send("Not playing any Games")
    
#run client
            
client.run('ODU1OTE5OTkwMjA5NTExNDQ0.YM5fmw.bDqgfAecYfgYqzyvtYa7IKiixtA')