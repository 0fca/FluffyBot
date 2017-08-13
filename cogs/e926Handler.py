import requests
from discord.ext import commands
from cogs.utils.scrappers import jsonScrapper
from cogs.utils.botErrors import BotErrors


class E621Handler(object):
    def __init__(self, bot):
        self.bot = bot
        self.search_link = 'http://e926.net/post/index.json?tags='
        self.entries = {}
        self.keys = ['file_url']
        self.errors = BotErrors.BotErrors() 

    @commands.command()
    async def e9(self, ctx):
        split_message = ctx.message.content.split()
        amount = self.get_amount(split_message)
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
    print('added E9 module')
    bot.add_cog(E621Handler(bot))
