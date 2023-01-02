import discord
from discord.ext import commands

client =  commands.Bot(command_prefix = ".")

@client.event
async def on_ready():
    print('bot is ready')

@client.command()
@commands.has_role('Admin')
async def clear(ctx, amount=5):
    await ctx.channle.purge(limit=amount)

@client.command()
@commands.has_role('Admin')
async def kick(ctx, member : discord.Member, reason=None):
    await member.kick(reason=reason)

@client.command()
@commands.has_role('Admin')
async def ban(ctx, member : discord.Member, reason=None):
    await member.ban(reason=reason)

@client.command()
async def hackerban(ctx, member : discord.Member, reason=None):
    await member.ban

    
client.run("ODEyNzc2MjA3NjQwNTU5Njkx.YDFq1A.TmsR_37216NHnjTb5-oLPndNTlo")