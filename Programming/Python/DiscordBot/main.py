import discord
from discord.ext import commands

client = commands.Bot(command_prefix='>') #What the bot listens to

@client.event
async def on_ready():
    print("Bot initalized")

#The token
client.run('NzYxNTkxNzA5ODk3MTk1NTMx.X3c1jQ.K51ExN9AVjPQ8GgVa3-qRloYuDM')