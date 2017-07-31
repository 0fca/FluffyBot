import requests
from discord.ext import commands

from cogs.utils.scrappers import jsonScrapper


class E621Handler(object):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.search_link = 'http://e926.net/post/index.json?tags='
        self.connection = '+'
        self.respond = ''
        self.entries = []

    @commands.command(pass_context=True)
    async def e9(self, ctx):
        amount = self.get_amount(ctx.message.content)
        query = self.get_query(ctx.message.content)
        print(amount)
        print(query)
        self.make_req(query)

        for i in range (0, amount):
            await self.bot.say(self.entries[i])


    def make_req(self, query):
        req_mess = self.search_link + query
        self.respond = requests.get(req_mess)
        self.parse_result(self.respond)

    def parse_result(self, result):
        keys = ['file_url']
        scrapper = jsonScrapper.jsonScrapper(keys, result.text)
        entries = scrapper.get_values(2)
        self.entries.clear()
        try:
            for item in entries[ keys[ 0 ] ]:
                self.entries.append(item[:5] + ':' + item[5:])
        except KeyError:
            print('dict is null')
    
    def get_amount(self, message):
        result = message.split()
        try:
            if result[1].isdigit() and int(result[1]) > 0:
                return int(result[1])
            else:
                return 1
        except IndexError:
            return 1
    def get_query(self, message):
        result = message.split()
        del result[0]
        if result[0].isdigit():
            del result[0]
        return '+'.join(result)


def setup(bot):
    print('added E9 module')
    bot.add_cog( E621Handler(bot) )
