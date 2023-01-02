import discord
from discord.ext import commands
import json
import os
intents = discord.Intents.all()
intents.members = True


directory = os.path.dirname(__file__)
os.chdir(directory)



client = commands.Bot(command_prefix = "?", intents=intents)
client.remove_command('help')
bad_words = ["nigga","nigger","sex","niga","niger",]
#Dianogstics:......................................................
@client.event
async def on_ready():
    activity = discord.Game(name="?help", type=3)
    await client.change_presence(status=discord.Status.online, activity=activity)
    print("Bot is ready!")


@client.command()
async def ping(ctx):
    await ctx.send('pong')





#Mod Commands:.........................................................
@client.command()
@commands.has_any_role(832000678418972712)
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)
    user = member 
    mod = ctx.author
    await open_account(user)
    users = await get_user_data()
    users[str(user.id)]['kicks'] += 1
    em = discord.Embed(title = f'{ctx.author.name}',color = discord.Color.red())
    await ctx.send(f'{user.mention} has been kicked for {reason}')
    await user.send(f"you have been Kicked for {reason}")

@client.command()
@commands.has_any_role(832000678418972712)
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'Banned {member.mention}')

@client.event 
async def on_message(msg):
    user = msg.author
    con = msg.content
    low = con.lower()
    ch = msg.channel
    for word in bad_words:
        if word in low:
            await msg.delete()
            await ch.send(f'I better see soap in that mouth rn {user.mention}')
    await client.process_commands(msg)

@client.command()
@commands.has_any_role(832000678418972712)
async def warn(ctx, member : discord.Member, *, reason=None):
    user =  member
    await open_account(user)


    users = await get_user_data()
    if reason == None:
        reason = "a unspecified reason"
    else:
        return
    
    await ctx.send(f"{member.mention} has been warned for {reason}")


    users[str(user.id)]['warns'] += 1
    with open("data.json","w") as f:
     json.dump(users,f)

@client.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount+1)
        
#Fun Commands:.........................................................
@client.command(name='setstatus', aliases=['ss', 'game'])
async def setstatus(ctx, status, game):
    gamerRole= discord.utils.get(ctx.guild.roles, name = "Gamer")
    author = ctx.author
    roles = author.roles
    if status == "no": 
        if gamerRole not in author.roles:
            await ctx.send('You cant do that dummy')
        else:
            await author.remove_roles(gamerRole)
            await author.send(f'Bye Bye {author.mention}')
    if status == "yes":
        if gamerRole in author.roles:
            await ctx.send('You cant do that dummy')
        else:
           await author.add_roles(gamerRole)
           await ctx.send(f"{gamerRole.mention} {author.mention} is now playing {game}" )

@client.event
async def on_member_join(mb):
    ch = client.get_channel(840017943769251882)
    ch.send(f"Welcome to MINETOPIA, OUR VERSION OF HELL, {mb.mention}")
    
    
# Profile:............................................................

async def open_account(user):
    users = await get_user_data()

    if str(user.id) in users:
        return False
    else:
        users[str(user.id)] = {}
        users[str(user.id)]['wallet'] = 0
        users[str(user.id)]['bank'] = 0
        users[str(user.id)]['warns'] = 0
        users[str(user.id)]['kicks'] = 0
        users[str(user.id)]['bans'] = 0
        with open("data.json","w") as f:
         json.dump(users,f)
    return True   

async def get_user_data():
    with open('data.json',"r") as f:
        users = json.load(f)
        return users

@client.command() 
async def pf(ctx):
    await open_account(ctx.author)
    user = ctx.author
    users = await get_user_data()
    wallet_amt = users[str(user.id)]['wallet']
    bank_amt = users[str(user.id)]['bank']
    em = discord.Embed(title = f'{ctx.author.name}',color = discord.Color.red())
    em.add_field(name = "Wallet",value = wallet_amt)
    em.add_field(name = "Bank ",value = bank_amt)
    await ctx.send(embed = em)

@client.command()
async def modpf(ctx, member : discord.Member):
    user = member
    await open_account(user)
    mod = ctx.author
    users = await get_user_data()
    warns_amt = users[str(user.id)]['warns']
    kick_amt = users[str(user.id)]['kick']
    ban_amt = users[str(user.id)]['Bans']
    em = discord.Embed(title = f'{user}',color = discord.Color.red())
    em.add_field(name = "Warns", value = warns_amt)
    em.add_field(name = "Kicks", value = kick_amt)
    em.add_field(name = "Bans", value = ban_amt)
    await mod.send(embed = em)

#economy.............................................................................................................................

async def editbank(user, change = 0, mode = "wallet"):
    users = await get_user_data()
    users[str(user.id)][mode] += change
    with open("data.json","w") as f:
        json.dump(users,f)   

    bal = users[str(user.id)]['wallet'], users[str(user.id)]['bank']
    return bal

   
@client.command()
async def wth(ctx, amount = None):
    await open_account(ctx.author)
    amount = int(amount)
    if amount == None:
        ctx.send('You cant take out nothin')
        return
    
    bal = await editbank(ctx.author)
    if amount>bal[1]:
        await ctx.send("You cant fool me, broke ass!!")
        return
    if amount<0:
        await ctx.send('Im not going to pay for that you debt ridden fuck!')

    
    await editbank(ctx.author, amount,'wallet')
    await editbank(ctx.author, -1*amount,'bank')
    await ctx.send(f"You withdrew {amount} from your bank!" )

@client.command()
async def dep(ctx, amount = None):
    await open_account(ctx.author)
    amount = int(amount)
    if amount == None:
        ctx.send('You cant take out nothin')
        return
    
    bal = await editbank(ctx.author)
    if amount>bal[0]:
        dif = bal[0]-amount
        await ctx.send(f"go get {dif} from your mum, ya broke child!!")
        return
    if amount<0:
        await ctx.send('Im not going to pay for that you debt ridden fuck!')

    
    await editbank(ctx.author, -1*amount,'wallet')
    await editbank(ctx.author, amount,'bank')
    await ctx.send(f"You deposited {amount} from your bank!" )    


@client.command()
async def give(ctx,user:discord.Member, amount = None):
    await open_account(ctx.author)
    await open_account(user)
    amount = int(amount)
    if amount == None:
        await ctx.send('Stop being stupid and actualy give somthing!')
        return
    
    bal = await editbank(ctx.author)
    if amount>bal[0]:
        dif = bal[0]-amount
        await ctx.send(f"You need to get {dif} before you can give that much!!")
        return
    if amount<0:
        await ctx.send('Go get a god damn job and stop being broke!!')

    
    await editbank(user, amount,'wallet')
    await editbank(ctx.author, -1*amount,'wallet')
    await ctx.send(f"You gave {amount} to {user}!" )




@client.command()
@commands.has_any_role(832000678418972712)
async def pay(ctx, amt):
    amt = int(amt)
    print("l")
    for user in ctx.guild.members:

        print("l")
        if user.bot == True:
            print("s")
        else:
            await open_account(user)
            print("l")
            await editbank(user, amt,'wallet')
            print("l")
            await ctx.send(f'{user.mention} was paid {amt}')
            print("l")


@client.command()
async def help(ctx,mode = None):
    if mode == "mod":
        em = discord.Embed(title = "Help",color = discord.Color.red())
        em.add_field(name = "?kick", value = "?kick <member> <reason>")
        em.add_field(name = "?warn", value = "?warn <member> <reason>")
        em.add_field(name = "?ban", value = "?ban <member> <reason>")
        em.add_field(name = "?modpf", value = "modpf <member>")
        em.add_field(name = "?pay", value= "?pay <member> <amount>")
        await ctx.author.send(embed = em)
        return
    elif mode == "game":
        em = discord.Embed(title = "Help",color = discord.Color.blue())
        em.add_field(name = "?setstatus", value = "?ss <yeas or no> <game>")
        await ctx.author.send(embed = em)
    elif mode == "money":
        em = discord.Embed(title = "Help",color = discord.Color.green())
        em.add_field(name = "?pf", value = "?pf (view your balance)")
        em.add_field(name = "?give", value = "?give <user> <amount>")
        em.add_field(name = "?wth", value = "?wth <amount>")
        em.add_field(name = "?dep", value = "?dep <amount>")
        await ctx.author.send(embed = em)
    elif mode == None:
        em = discord.Embed(title = "Help",color = discord.Color.dark_blue())
        em.add_field(name = "mod", value = 'Moderator')
        em.add_field(name = "money", value = 'Money')
        em.add_field(name = "game", value = 'Game')
        em.add_field(name = "?help", value = "?help <select a catagory above>")
        await ctx.author.send(embed = em)

@client.command()
async def test(ctx):
    for user in ctx.guild.members:
        print(user)

    

    

    

    



        


    

#ODM2MjkxNjM3MzQ3ODc2OTA1.YIb3Rw.iu6toY49HtRetlz4TzKBTWf2dyY stable build
#ODM4ODcyNzYzMzc2NTk5MDUw.YJBbJA.Gu3-_YFbJ7FmewXZYabuUUq2qx8 test build

client.run('ODM4ODcyNzYzMzc2NTk5MDUw.YJBbJA.Gu3-_YFbJ7FmewXZYabuUUq2qx8')
