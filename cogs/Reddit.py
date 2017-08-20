import requests
import random
from discord.ext import commands
import cogs.utils.configJSON as configJson
from cogs.utils.scrappers import jsonScrapper


class Reddit(object):
    def __init__(self, bot):
        self.bot = bot
        self.imgur_link = "https://api.imgur.com/3/gallery/r/"
        self.entries = {}
        self.keys = ['link']

    @commands.command()
    async def dailysnek(self, ctx):

        self.make_req(self.imgur_link, "snek")
        i = random.randint(0, len(self.entries['link']))
        await ctx.send(self.entries['link'][i])

    @commands.command()
    async def dailydoggo(self, ctx):

        self.make_req(self.imgur_link, "doggos")

    @commands.command()
    async def dailydoge(self, ctx):

        self.make_req(self.imgur_link, "doge")
        i = random.randint(0, len(self.entries['link']))
        await ctx.send(self.entries['link'][i])

    @commands.command()
    async def dailyaww(self, ctx):

        self.make_req(self.imgur_link, "aww")
        i = random.randint(0, len(self.entries['link']))
        await ctx.send(self.entries['link'][i])

    @commands.command()
    async def eyebleach(self, ctx):

        self.make_req(self.imgur_link, "eyebleach")
        i = random.randint(0, len(self.entries['link']))
        await ctx.send(self.entries['link'][i])


    def make_req(self, link, subreddit=''):
        headers = {'authorization': 'Client-ID ' + configJson.imgur_token}
        req_message = requests.request('GET', link + subreddit, headers=headers)
        self.parse_req(req_message.text)

    def parse_req(self, response):
        scrapper = jsonScrapper.jsonScrapper(self.keys, response)
        self.entries.clear()
        self.entries = scrapper.get_values("imgur")


def setup(bot):
    print("Added Reddit module")
    bot.add_cog(Reddit(bot))
