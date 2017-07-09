import requests
import re

from discord.ext import commands



class derpi(object):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.search_link = 'https://derpibooru.org/search.json?q='
        self.connection = '+'
        self.respond = ''

    @commands.command(pass_context = True)
    async def dp(self, ctx):
        pass

    def amount(self, message):
        result = re.findall('\/{2}dp\s\d+', message)
        try:
            number = int(result[0][5:])
        except Exception:
            return 1

        if number > 0:
            return number
        else:
            return 1

def setup(bot):
    bot.add_cog(derpi(bot))