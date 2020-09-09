import random

@client.command(aliases= ['8ball'])
async def eightball(ctx, *, question):
    responses = ["As I see it, yes.",
                'Ask again later.',
                'Better not tell you now.',
                'Cannot predict now.',
                "Concentrate and ask again.",
                "Don't count on it.",
                "It is certain.",
                "It is decidedly so."]
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')
