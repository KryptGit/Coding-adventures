import discord
from discord.ext import commands



client = commands.Bot(command_prefix = "?")


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
client.run('OTI4MTIzMDY0MTU0MjAyMTEz.YdUL9g.9TdhFnbv-1oHy41_QLvmgm8-t44')
