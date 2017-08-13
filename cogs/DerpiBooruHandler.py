import requests
from discord.ext import commands

from cogs.utils.scrappers import jsonScrapper


class DerpiBooru(object):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.search_link = 'https://derpibooru.org/search.json?q='
        self.connection = '+'
        self.respond = ''
        self.entries = {}
        self.keys = ['image']

    @commands.command(pass_context=True)
    async def dp(self, ctx):
        split_message = ctx.message.content.split()
        amount = self.get_amount(split_message)
        query = self.get_query(split_message)
        self.make_req(query)

        for i in range(amount):
            await ctx.send(self.entries[self.keys[0]][i])

    def make_req(self, query):
        req_mess = self.search_link + query
        self.respond = requests.get(req_mess)
        
        self.parse_result(self.respond)

    def parse_result(self, result):
        scrapper = jsonScrapper.jsonScrapper(self.keys, result.text)
        self.entries.clear()
        self.entries = scrapper.get_values("dp")

    @staticmethod
    def get_amount(message_split):
        try:
            return  int(message_split[1]) if message_split[1].isdigit() and int(message_split[1]) > 0 else 1
        except IndexError:
            return 1

    @staticmethod
    def get_query(message_split):
        #try not deleting it
        del message_split[0]
        if message_split[0].isdigit():
            del message_split[0]
        return '+'.join(message_split)


def setup(bot):
    print("added DP module")
    bot.add_cog(DerpiBooru(bot))

