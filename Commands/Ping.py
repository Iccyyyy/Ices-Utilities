@client.command()
async def ping(ctx):
    await ctx.send(f"Pong! `{round(client.latency * 1000)}ms`")
