import requests
from discord.ext import commands

from cogs.utils.scrappers import jsonScrapper


class DerpiBooru(object):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.search_link = 'https://derpibooru.org/search.json?q='
        self.connection = '+'
        self.respond = ''
        self.entries = []

    @commands.command(pass_context=True)
    async def dp(self, ctx):
        amount = self.get_amount(ctx.message.content)
        query = self.get_query(ctx.message.content)
        self.make_req(query)

        for i in range(0, amount + 1 ):
            await self.bot.say(self.entries[i])

    def make_req(self, query):
        req_mess = self.search_link + query
        self.respond = requests.get(req_mess)
        self.parse_result(self.respond)

    def parse_result(self, result):
        keys = ['image']
        scrapper = jsonScrapper.jsonScrapper(keys, result.text)
        entries = scrapper.get_values()
        self.entries.clear()
        for item in entries[keys[0]]:
            self.entries.append("https:" + item)

    def get_amount(self, message):
        result = message.split()
        try:
            if result[1].isdigit() and int(result[1]) > 0:
                print(result[1])
                return int(result[1])
            else:
                return 1
        except IndexError:
            return 1

    def get_query(self, message):
        result = message.split()
        # delete command
        del result[0]
        if result[0].isdigit():
            # delete number of entries to show if they exist
            del result[0]
        return '+'.join(result)


def setup(bot):
    print("added DP module")
    bot.add_cog(DerpiBooru(bot))

