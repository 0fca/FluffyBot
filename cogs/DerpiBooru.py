import requests
from discord.ext import commands

from cogs.utils.scrappers import jsonScrapper


class DerpiBooru(object):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.search_link = 'https://derpibooru.org/search.json?q='
        self.entries = {}
        self.keys = ['image']

    @commands.command()
    async def dp(self, ctx, *, args: str):
        split_message = args.split()

        amount = int(split_message[-1]) if split_message[-1].isdigit() and int(split_message[-1]) > 0 else 1
        query = self.get_query(split_message)
        self.make_req(query)

        for i in range(amount):
            await ctx.send(self.entries[self.keys[0]][i])

    def make_req(self, query):
        req_mess = self.search_link + query
        respond = requests.get(req_mess)

        self.parse_result(respond)

    def parse_result(self, result):
        scrapper = jsonScrapper.jsonScrapper(self.keys, result.text)
        self.entries.clear()
        self.entries = scrapper.get_values("dp")

    @staticmethod
    def get_query(message_split):
        # try not deleting it
        if message_split[-1].isdigit():
            del message_split[-1]
        return '+'.join(message_split)


def setup(bot):
    print("added DP module")
    bot.add_cog(DerpiBooru(bot))
