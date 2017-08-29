import wikipedia
from discord.ext import commands


class wiki(object):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def wiki(self, ctx, *, args: str):
        search = wikipedia.search(args)

        if len(search) > 0:
            await ctx.send(wikipedia.summary(search[0]))
        else:
            await ctx.send("I didn't find anything, sorry. Try something else")


def setup(bot):
    print("added wiki module")
    bot.add_cog(wiki(bot))
