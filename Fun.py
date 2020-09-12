import discord
from discord.ext import commands
import os
import random


class Fun(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Fun is loaded.")      




    @commands.command(aliases= ['8ball'])
    async def eightball(self, ctx, *, question):
        responses = ["As I see it, yes.",
                'Ask again later.',
                'Better not tell you now.',
                'Cannot predict now.',
                "Concentrate and ask again.",
                "Don't count on it.",
                "It is certain.",
                "It is decidedly so."]
        await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')  


    @eightball.error
    async def eightball_error(self, ctx, error):
        if isinstance(error,commands.MissingRequiredArgument):
            await ctx.send("Please use ?8ball [question]")







def setup(client):
    client.add_cog(Fun(client))