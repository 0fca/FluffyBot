from discord.ext import commands

class HelpModule(object):

    def __init__(self, bot):
        self.bot = bot
        self.cogs = {}


    async def send_cmd_list(self):
        cmd_list = ''


def setup(bot):
    print("Added HelpModule")
    bot.add_cog(HelpModule(bot))
