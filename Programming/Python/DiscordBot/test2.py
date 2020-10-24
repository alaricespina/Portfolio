import discord
import time

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
    
    if message.content.startswith('$Hatdog'):
        await message.channel.send('mo maliit')

    if message.content.startswith('$help'):
        embed = discord.Embed(title="Help on BOT", description="Some useful commands")
        embed.add_field(name="$hello", value="Greets the user")
        embed.add_field(name="$Hatdog", value="You know the answer")

        await message.channel.send(content=None, embed=embed)

    if message.content.startswith('$leave'):
        print("sleeping for 10s")
        time.sleep(10)
        print("sleep done")

    if message.content.startswith('$$quit'):
        await client.close()

#Bot not stopping

client.run('NzYxNTkxNzA5ODk3MTk1NTMx.X3c1jQ.6dJF6Xe0hPaoIRZp4BsTeHO3nHs')