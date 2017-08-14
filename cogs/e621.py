import requests
from discord.ext import commands
from cogs.utils.scrappers import jsonScrapper
from cogs.utils.botErrors import BotErrors
from cogs.utils import  checks


class E621:
    def __init__(self, bot):
        self.bot = bot

        self.search_link = 'http://e621.net/post/index.json?tags='
        self.entries = {}
        self.keys = ['file_url']

        self.errors = BotErrors.BotErrors()
        self.check = checks.checks()

    @commands.command()
    async def e6(self, ctx, *,arg: str):
        # don't do anything we are not in nsfw channel
        if ctx.channel.is_nsfw():
            split_message = arg.split()

            amount = int(split_message[-1]) if split_message[-1].isdigit() and int(split_message[-1]) > 0 else 1
            query = self.get_query(split_message)

            if "loli" in split_message and not self.check.is_loli(ctx.channel):
                await ctx.send(self.errors.NotLoliChannel())
                return

            # we are clean, search for this porn
            self.make_req(query,amount)

            for entry in self.entries[self.keys[0]]:
                await ctx.send(entry)

        else: await ctx.send(self.errors.NotNSFWChannel())

    def make_req(self, query, amount):
        req_mess = self.search_link + query + "&limit=" + str(amount)
        respond = requests.get(req_mess)

        self.parse_result(respond)

    def parse_result(self, result):
        scrapper = jsonScrapper.jsonScrapper(self.keys, result.text)
        self.entries.clear()
        self.entries = scrapper.get_values("e6")

    @staticmethod
    def get_query(message_split):
        # try not deleting it
        if message_split[-1].isdigit():
            del message_split[-1]
        return '+'.join(message_split)


def setup(bot):
    print("Added E6 module")
    bot.add_cog(E621(bot))