from discord.ext import commands

class HelpModule(object):

    def __init__(self, bot, cogs):
        self.bot = bot
        self.cogs = cogs

    @commands.command()
    async def help(self, ctx):
        await ctx.send("empire did nothing wrong!")


def setup(bot):
    print("Added HelpModule")
    bot.remove_command("help")
    bot.add_cog(HelpModule(bot, bot.cogs))
