import discord

import random

from discord.ext import commands

import math

from sympy import symbols

from discord import Webhook, AsyncWebhookAdapter

import aiohttp

a, b, x, y, z = symbols('a b x y z')

bot = commands.Bot(command_prefix='*',

    description='A bot Reginald made for fun in python',

    owner_id=729433621533819000,

    case_insensitive=True,)

@bot.event

async def on_ready():

    P = ['Aliens', 'Sus', 

         'Terraria on CNN with Reginald and Right Hand Man', 'Henry Stickmin hijacking The Toppat Orbital Station', 'The Area 51 raid']

    dhs = ['https://www.grubhub.com', 'https://www.youtube.com/watch/dQw4w9WgXcQ']

    await bot.change_presence(status=discord.Status.online, activity=discord.Streaming(name=f'{random.choice(P)} | do *help | in ' + str(len(bot.guilds)) + ' servers', url=f'{random.choice(dhs)}'))

    print('We have logged in as {0.user}'.format(bot))

@bot.command()

async def twoball(ctx, *, question):

    """- fun command that possesses TPOT (The Power Of Two)"""

    answers = ['It is certain.', 'It is decidedly so.',

               'without a doubt.', 'Yes - definitely.',

               'Most likely.', 'Outlook good.',

               'Yes.', 'Signs point to yes.',

               'Reply hazy, try again', 'Ask again later.',

               'Better not tell you now.', 'Cannot predict now.',

               'Concentrate and ask again.', 'Don\'t count on it.',

               'My reply is no.', 'My sources say no.',

               'Outlook not so good.', 'Very doubtful.',

               'Signs point to no.', 'The answer is no.']

    await ctx.send(f"Question: {question}\nAnswer: {random.choice(answers)}")

    

@bot.command()

async def fnfbad(ctx):

    """- says that Friday Night Funkin' is bad"""

    answers = ['It is certain.', 'It is decidedly so.',

               'without a doubt.', 'Yes - definitely.',

               'Most likely.', 'Outlook good.',

               'Yes.', 'Signs point to yes.',]

    await ctx.send(f"{random.choice(answers)}")

  

@bot.command()

async def grubhub(ctx):

    """- GRUBHUB!!!!!!!"""

    embed = discord.Embed(title="GRUBHUB!", url="https://www.grubhub.com", description="FOOD", color=0x0000FF) 

    embed.set_thumbnail(url="https://i.kym-cdn.com/photos/images/newsfeed/001/993/720/ee1.png")

    await ctx.send(embed=embed)

    

@bot.command()

async def foo():

    async with aiohttp.ClientSession() as session:

        webhook = Webhook.from_url('https://discord.com/api/webhooks/803482984052949042/vCqvvkzwrFthdIhs7cQlM-5Y2K4XpLOO6Xu0zJqddRTjP0drOQl6nN21IWcgSHB3Alj6', adapter=AsyncWebhookAdapter(session))

        await webhook.send('Hello World', username='Foo')

  

@bot.command() 

async def add(ctx, x: int, y: int):

    """- Addition"""

    await ctx.send(f"{x}+{y}={x + y}")

    

@bot.command() 

async def minus(ctx, x: int, y: int):

    """- Subtraction"""

    await ctx.send(f"{x}-{y}={x - y}")

    

@bot.command() 

async def anything(ctx):

    """- Something"""

    await ctx.send("anything")

  

@bot.command()

async def invite(ctx):

	"""- Invite the bot to your server"""	embed = discord.Embed(title="Invite to server", url="https://discord.com/api/oauth2/authorize?client_id=782052137713664000&permissions=2147483639&redirect_uri=https%3A%2F%2Fdiscord.com%2Fapi%2Foauth2%2Fauthorize%3Fclient_id%3D782052137713664000%26permissions%3D8%26scope%3Dbot&scope=bot")

	await ctx.send(embed=embed)

	

@bot.command()  

async def botservers(ctx):

    """- The amount of servers the bot is in"""

    await ctx.send("I'm in " + str(len(bot.guilds)) + " servers")

  

@bot.command()

async def hai(ctx):

    """- link to the Half As Intresting channel if you need it"""

    await ctx.send("https://youtube.com/c/halfasinteresting")

    

@bot.command()

async def rickroll(ctx):

    """- rick roll link"""

    await ctx.send("https://youtu.be/dQw4w9WgXcQ")

    

@bot.command() 

async def multiply(ctx, x: int, y: int):

    """- Multiplication"""

    await ctx.send(f"{x}×{y}={x * y}")

    

@bot.command() 

async def ik(ctx):

    """- You know that already"""

    await ctx.send("Ok")

    

bot.run('TOKEN')
