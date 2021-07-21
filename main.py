import random
import discord
from discord.embeds import Embed
from discord.ext import commands
import utils

# load the token from a private file 
TOKEN = open(".secret").read()  

# Set intents
intents = discord.Intents.default()
intents.members = True

# Create a bot instance
client = discord.Client(intents=intents)

# Client Events

@client.event
async def on_ready():
    print('Logged in as ' + client.user.name)

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    # Eight Ball 🎱
    elif message.content.startswith('🎱'):
        await message.channel.send(utils.eight_ball())

    # Roll Dice 🎲
    elif '🎲' in message.content:
        await message.channel.send(utils.roll_dice(message.content))

# DM new members a welcome message
@client.event
async def on_member_join(member):
    embed = discord.Embed(
        title=f"Welcome {member.name}",
        description=f"Thanks for joining {member.guild.name}, it would be awesome if you could change your nickname to include your name and major and then introduce yourself so that we can get to know you!"
    )

    await member.create_dm()
    await member.dm_channel.send(embed=embed)

# Run The Bot
client.run(TOKEN)
