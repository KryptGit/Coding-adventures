import discord
from discord.ext import commands



client = commands.Bot(command_prefix = "?")
x = True

@client.event
async def on_ready():
    print("Bot is ready!")
@client.command()
async def ping(ctx):
    await ctx.send('pong')
@client.command()
async def AI(ctx):
    while True:
        speeach = input("talk")
        await ctx.send(speeach)
@client.command()
async def spam(ctx):
    x = True
    while x == True:
        await ctx.send("HAHAHA")
@client.command()
async def off(ctx):
    x = False

client.run('OTI4MTIzMDY0MTU0MjAyMTEz.YdUL9g.XibpvaorG0zZ7fObfJlmXPKE0bA')
