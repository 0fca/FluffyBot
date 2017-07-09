import requests
import json
from discord.ext import commands


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

        for i in range(0, amount):
            await self.bot.say(self.entries[i])

    def make_req(self, query):
        req_mess = self.search_link + query
        self.respond = requests.get(req_mess)
        self.parse_result(self.respond)

    def parse_result(self, result):
        entries =  json.loads(result.content)
        for entry in entries['search']:
            self.entries.append("http:"+entry['image'])

    def get_amount(self, message):
        result = message.split()
        try:
            if result[1].isdigit():
                number = int(result[1])
                if number > 0:
                    return number
                else:
                    return 1
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
    print("added DP module")
    bot.add_cog(DerpiBooru(bot))
