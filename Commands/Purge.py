@client.command(aliases= ['clear'])
async def purge(ctx, amount=3):
    await ctx.channel.purge(limit=amount + 1)
