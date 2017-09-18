import aiohttp
import random
from discord.ext import commands
from collections import defaultdict
import cogs.utils.configJSON as configJson


class Reddit(object):
    def __init__(self, bot):
        self.bot = bot
        self.imgur_link = "https://api.imgur.com/3/gallery/r/"
        self.entries = defaultdict(list)
        self.keys = ['link']

    @commands.command()
    async def dailysnek(self, ctx):

        await self.make_req(self.imgur_link, "snek")
        i = random.randint(0, len(self.entries['link']))
        await ctx.send(self.entries['link'][i])

    @commands.command()
    async def dailydoggo(self, ctx):
        await self.make_req(self.imgur_link, "doggos")
        i = random.randint(0, len(self.entries['link']))
        await ctx.send(self.entries['link'][i])

    @commands.command()
    async def dailydoge(self, ctx):
        await self.make_req(self.imgur_link, "doge")
        i = random.randint(0, len(self.entries['link']))
        await ctx.send(self.entries['link'][i])

    @commands.command()
    async def dailyaww(self, ctx):
        await self.make_req(self.imgur_link, "aww")
        i = random.randint(0, len(self.entries['link']))
        await ctx.send(self.entries['link'][i])

    @commands.command()
    async def eyebleach(self, ctx):
        await self.make_req(self.imgur_link, "eyebleach")
        i = random.randint(0, len(self.entries['link']))
        await ctx.send(self.entries['link'][i])

    async def make_req(self, link, subreddit=''):
        headers = {'authorization': 'Client-ID ' + configJson.imgur_token}
        req_message = '{l}{s}'.format(l=link, s=subreddit)
        async with aiohttp.ClientSession(headers=headers) as cs:
            async with cs.get(req_message) as r:
                entries = await r.json()
                for entry in entries['data']:
                    for key in self.keys:
                        self.entries[key].append(entry[key])


def setup(bot):
    print("Added Reddit module")
    bot.add_cog(Reddit(bot))
