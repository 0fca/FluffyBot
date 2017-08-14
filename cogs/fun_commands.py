import random
from discord.ext import commands
from cogs.utils.botErrors import BotErrors
from cogs.utils.checks import checks

class fun_commands(object):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.botError = BotErrors.BotErrors()
        self.reactions = {
            'fuckthisshit': 'https://www.youtube.com/watch?v=5FjWe31S_0g',
            'crusade': 'https://www.youtube.com/watch?v=Ky2UP5j_pK8'}
        self.checks = checks()

    @commands.command()
    async def boop(self, ctx):
        if len(ctx.message.content) > 6:
            await ctx.send('boops ' + ctx.message.content[6:])
        else:
            await ctx.send('boops ' + ctx.message.author.mention)

    @commands.command()
    async def kill(self, ctx):
        if len(ctx.message.content) > 6:
            await ctx.send('kills' + ctx.message.content[6:])
        else:
            await ctx.send(ctx.message.author.mention + ' commits suicide')

    @commands.command()
    async def reaction(self, ctx):
        reaction = ctx.message.content[11:].lower()
        if reaction in self.reactions:
            await ctx.send(self.reactions[reaction])

    @commands.command()
    async def dearGod(self, ctx):
        # in the name of god - powerwolfSS
        await ctx.send('https://www.youtube.com/watch?v=mobtxEJHhY4')

    @commands.command()
    async def crusade(self, ctx):
        random_quotes = ['Non omnis moriar!',
                         'DEUS VULT',
                         'It\'s crusade time!',
                         'I feel like I need a crusade',
                         'It\'s a perfect day for a crusade',
                         'What a lovely time for a crusade']
        await ctx.send(random.choice(random_quotes) + '\n' + 'https://www.youtube.com/watch?v=Ky2UP5j_pK8')

    @commands.command()
    async def fuckthis(self,ctx):
        random_quotes = ['Man...',
                         "ARE YOU FUCKING KIDDING ME?!",
                         " ",
                         "well...",
                         "..."]
        await ctx.send(random.choice(random_quotes) + '\n' + 'https://www.youtube.com/watch?v=5FjWe31S_0g')

    @commands.command()
    async def ayylmao(self, ctx):
        ayylmao_repo = [
            'https://goo.gl/MKwbm9',
            'https://goo.gl/gNmzUH',
            'https://goo.gl/rRBVDf'
        ]
        rand = random.choice(range(0, len(ayylmao_repo)))
        await ctx.send(ayylmao_repo[rand])

    @commands.command()
    async def itsimportant(self,ctx):
        await ctx.send('https://www.youtube.com/watch?v=q6EoRBvdVPQ&list=PL7XlqX4npddfrdpMCxBnNZXg2GFll7t5y')

    @commands.command()
    async def yee(self, ctx):
        await ctx.send('https://youtu.be/q6EoRBvdVPQ')

    @commands.command()
    async def stop(self, ctx):
        await ctx.send('https://www.youtube.com/watch?v=2k0SmqbBIpQ')

    @commands.command()
    async def ping(self, ctx):
        await ctx.send('Pong!')

    @commands.command()
    async def nsfw(self, ctx):
        if ctx.channel.is_nsfw():
           await ctx.send("hello")
        else: await ctx.send(self.botError.NotNSFWChannel())

    @commands.command()
    async def loli(self, ctx):
        if self.checks.is_loli(ctx.message.channel):
            await ctx.send("loli time")
        else: await ctx.send(self.botError.NotLoliChannel())

    @commands.command()
    async def sendpm(self, ctx):
        # get all the cogs, and all it's commands to dict
        # if subcommand was not invoked, then send list of them, and
        # encurage user to choose about which one he want to read
        # show him example
        # send him everything via PM

        user = ctx.author
        await user.send("hi")


def setup(bot):
    print("added UserUtils module")
    bot.add_cog(fun_commands(bot))
