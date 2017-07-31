from discord.ext import commands


class HelpModule(object):

    def __init__(self, bot):
        self.bot = bot
        #find a way to get description from all all classes in cogs and store it in the dict
        self.description = {}

    @commands.group(pass_context = True, no_pm = True)
    async def help(self,ctx):
        if ctx.invoked_subcommand is None:
            await self.send_cmd_list()

    async def send_cmd_list(self):
        cmd_list = ''


def setup(bot):
    bot.add_cog(HelpModule(bot))
