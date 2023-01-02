import discord
from discord.ext import commands
import json
import os
directory = os.path.dirname(__file__)
os.chdir(directory)



client = commands.Bot(command_prefix = "?")
x = True

@client.event
async def on_ready():
    print("Bot is ready!")
@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! Server Ping:',round(client.latency * 1000),'ms')
@client.command()
async def myBdayis(ctx, bday):

client.run('OTI4MTIzMDY0MTU0MjAyMTEz.YdUL9g.XibpvaorG0zZ7fObfJlmXPKE0bA')
