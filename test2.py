import discord
from discord.ext.commands import Bot
from discord import Member

for activity in member.activities:
            if isinstance(activity, Game):
                name = activity.name
                Type = "Playing"
                Activity = f"{name}"
            elif isinstance(activity, Streaming):
                name2 = activity.name
                name3 = activity.platform
                Type = "Streaming"
                Activity = f"{name2} on {name3}"
            elif isinstance(activity, Spotify):
                name4 = activity.title
                name5 = activity.artists
                Type = "Listening to Spotify"
                Activity = f"**Song Name**:{name4}\n**Song Artists:**{name5}"
            elif isinstance(activity, CustomActivity):
                name6 = activity.name
                Type = "Custom Status"
                Custom = f"{name6}"
            else:
                name7 = activity.name
                Type =  "Playing"
                Activity = f"{name7}"


client.run('ODU1OTE5OTkwMjA5NTExNDQ0.YM5fmw.bDqgfAecYfgYqzyvtYa7IKiixtA')