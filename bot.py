import discord
import os
from discord.ext import commands, tasks
from discord.ext.commands import Bot
from itertools import cycle
import asyncio

client = commands.Bot(command_prefix = '?')



@client.event
async def on_ready():
    print("Bot is online!")
    while True:
        await client.change_presence(activity=discord.Activity(name="?help", type=1))
        await asyncio.sleep(60)
		
        await client.change_presence(activity=discord.Activity(name="Echidna..", type=3))
        await asyncio.sleep(60)

        await client.change_presence(activity=discord.Activity(name="Bot Developed by Ice!", type=1))
        await asyncio.sleep(60)
		
    




for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run("token")   
