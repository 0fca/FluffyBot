import requests
from discord.ext import commands
from cogs.utils.scrappers import jsonScrapper


class E926(object):
    def __init__(self, bot):
        self.bot = bot
        self.search_link = 'http://e926.net/post/index.json?tags='
        self.entries = {}
        self.keys = ['file_url']

    @commands.command()
    async def e9(self, ctx, *, arg: str):
        split_message = arg.split()

        amount = int(split_message[-1]) if split_message[-1].isdigit() and int(split_message[-1]) > 0 else 1
        query = self.get_query(split_message)

        self.make_req(query, amount)

        for entry in self.entries[self.keys[0]]:
            await ctx.send(entry)

    def make_req(self, query, amount):
        req_mess = self.search_link + query + "&limit=" + str(amount)
        respond = requests.get(req_mess)

        self.parse_result(respond)

    def parse_result(self, result):
        scrapper = jsonScrapper.jsonScrapper(self.keys, result.text)
        self.entries.clear()
        self.entries = scrapper.get_values("e9")

    @staticmethod
    def get_query(message_split):
        # try not deleting it
        if message_split[-1].isdigit():
            del message_split[-1]
        return '+'.join(message_split)


def setup(bot):
    print('added E9 module')
    bot.add_cog(E926(bot))
