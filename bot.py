# bot.py
import os

import discord
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')


questions = list()
with open('questions.txt', 'r') as f:
    questions = x = f.read().splitlines()

bot = commands.Bot(command_prefix='?')

writin=False


def f(x):
    return {
        0: '0️⃣',
        1: "1️⃣",
        2: '2️⃣',
        3: '3️⃣',
        4: '4️⃣',
        5: '5️⃣',
        6: '6️⃣',
        7: '7️⃣',
        8: '8️⃣',
        9: '9️⃣',
        10: '🔟'
    }.get(x, '0️⃣')

@bot.event
async def on_ready():
    for guild in bot.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{bot.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )


@bot.command()
async def ask(ctx, *, arg):

    llen = len(questions)

    q =str(llen+1)+". "+ str(ctx.message.author.name)+": "+str(arg)
    questions.append(q)   

    #await ctx.send("added to list now "+ str(len(questions)) +" questions")
    await ctx.message.add_reaction("🤖")

    k=0
    for i in str(llen+1):

        if k>0:
            if str(llen+1)[k-1]==str(llen+1)[k]:
                await ctx.message.add_reaction("⬅")
                
            else:
                await ctx.message.add_reaction(f(int(i)))
        else:
            await ctx.message.add_reaction(f(int(i)))
        
        k=k+1

    backup()
   
    
    
    
    
    
    
def updatenum():
    updated=list()

    lenq=len(questions)

    for q in reversed(questions):

        x = str(lenq)+". "+q.split(". ",1)[1]
        lenq=lenq-1
        updated.append(x)
    
    questions.clear()
    updated.reverse()
    questions.extend(updated)




def backup():
    with open('questions.txt', 'w') as f:
        for item in questions:
            f.write("%s\n" % item)


@bot.command()
async def ls(ctx):
    listlen=len(questions)

    if listlen>=1:
       
        resp = "\n".join(str(x) for x in questions)

    else:
        resp="List is empty add a question with ?ask "
    await ctx.send(str(resp))

@bot.command()
async def lsrem(ctx, torm):
    try:
        questions.pop(int(torm)-1)
        respp = "removed now: " + str(len(questions))+" items"
        updatenum()
        backup()
    except ValueError:
        role1 = discord.utils.get(ctx.guild.roles, name="Admin")
        role2 = discord.utils.get(ctx.guild.roles, name="Moderator")
        #print(str(ctx.author.roles))
        if str(torm) == "all" and ((role1 in ctx.author.roles) or (role2 in ctx.author.roles)):
            questions.clear()
            backup()
            respp = "List cleared"
        else:
            return
    except IndexError:
        return
    await ctx.send(respp)
        

@bot.command()
async def info(ctx):
    embed = discord.Embed(
        title="ListBot3000", description="Beep boop I make lists.", color=0xeee657)
    embed.add_field(name="Author", value="@ThePr0grammer")
    await ctx.send(embed=embed)

bot.remove_command('help')


@bot.command()
async def help(ctx):
    embed = discord.Embed(
        title="List Bot 3000", description="Beep boop I make lists. List of commands are:", color=0xeee657)
    embed.add_field(
        name="?ask Is cereal soup?", value="Adds a question to the list.", inline=False)
    embed.add_field(name="?ls",
                    value="Shows the list of questions.", inline=False)
    embed.add_field(
        name="?lsrem 1", value="Removes a question from the list.", inline=False)
    embed.add_field(
        name="?lsrem all", value="Clears the list works only for Mods.", inline=False)

    embed.add_field(
        name="?info", value="Gives a little info about the bot.", inline=False)
    embed.add_field(name="?help", value="Gives this message", inline=False)

    await ctx.send(embed=embed)

bot.run(TOKEN)
