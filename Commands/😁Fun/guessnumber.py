@client.command()
async def guessthenumber(ctx):
    computer = random.randint(1, 10)
    await ctx.send("Guess my number. It could be any from 1 to 10.")

    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel and int(msg.content) in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    msg = await client.wait_for("message", check=check)

    if int(msg.content) == computer:
        await ctx.send("Correct")
    else:
        await ctx.send(f"Nope it was {computer}")
