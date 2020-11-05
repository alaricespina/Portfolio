import discord
from discord.ext import commands

guilds = []

bot = commands.Bot(command_prefix='>') #What the bot listens to

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

@bot.command()
async def test(ctx, arg):
    await ctx.send(arg)

@bot.command()
async def leave(ctx):
    await bot.logout()

@bot.command()
async def gcreate(ctx, arg):
    if arg not in guilds:
        guilds.append(arg)
        await ctx.send(f"Guild {arg} has been created")
    else:
        await ctx.send("Guild already in list")

@bot.command()
async def showguilds(ctx):
    for x in guilds:
        await ctx.send(x)

    
#The token
bot.run('NzcxMzc1NjUzOTM3MjE3NTk4.X5rNjw.oslcr4m5J24lflzePv5y2aCYbf8')