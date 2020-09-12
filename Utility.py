import discord
from discord.ext import commands
import os

class Utility(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Utility is loaded.")


    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f"Pong! `{round(self.client.latency * 1000)}ms`")




def setup(client):
    client.add_cog(Utility(client))