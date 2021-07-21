import random
import discord
from discord.ext import commands

# load the token from a private file 
TOKEN = open(".secret").read()  

# Create a bot instance
bot = commands.Bot(command_prefix="!")
client = discord.Client()


@bot.command(name='🎱')
async def nine_nine(context):
    """Ask the Magic 8-Ball a question"""
    possible_responses = ['It is certain','It is decidedly so','Without a doubt','Yes, definitely','You may rely on it','As I see it, yes','Most likely','Outlook good','Yes','Signs point to yes','Reply hazy try again','Ask again later','Better not tell you now', 'Cannot predict now','Concentrate and ask again','Don\'t count on it','My reply is no','My sources say no','Outlook not so good','Very doubtful']
    await context.send(random.choice(possible_responses))

@bot.command(name='repeat')
async def repeat(context, *, message: str):
    await context.send(message)

@bot.command(name='repeat_args')
async def repeat_args(context, *args):
    [print(i) for i in args]
    await context.send(' '.join(args))


bot.run(TOKEN)
