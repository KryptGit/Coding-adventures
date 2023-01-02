import discord
from discord.ext import commands



client = commands.Bot(command_prefix = "?")
x = True

@client.event
async def on_ready():
    print("Bot is ready!")
    

client.run('OTI4MTIzMDY0MTU0MjAyMTEz.YdUL9g.XibpvaorG0zZ7fObfJlmXPKE0bA')
