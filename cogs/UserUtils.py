import random
from discord.ext import commands


class UserUtils(object):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.reactions = {
            'fuckthisshit': 'https://www.youtube.com/watch?v=5FjWe31S_0g',
            'crusade': 'https://www.youtube.com/watch?v=Ky2UP5j_pK8'}

    @commands.command(pass_context=True)
    async def boop(self, ctx):
        if len(ctx.message.content) > 6:
            await self.bot.say('boops ' + ctx.message.content[6:])
        else:
            await self.bot.say('boops ' + ctx.message.author.mention)

    @commands.command(pass_context=True)
    async def kill(self, ctx):
        if len(ctx.message.content) > 6:
            await self.bot.say('kills' + ctx.message.content[6:])
        else:
            await self.bot.say(ctx.message.author.mention + ' commits suicide')

    @commands.command(pass_context=True)
    async def reaction(self, ctx):
        reaction = ctx.message.content[11:].lower()
        if reaction in self.reactions:
            await self.bot.say(self.reactions[reaction])

    @commands.command()
    async def crusade(self):
        random_quotes = ['Non omnis moriar!',
                         'DEUS VULT',
                         'It\'s crusade time!',
                         'I feel like I need a crusade',
                         'It\'s a perfect day for a crusade',
                         'What a lovely time for a crusade']
        await self.bot.say(random.choice(random_quotes) + '\n' + 'https://www.youtube.com/watch?v=Ky2UP5j_pK8')

    @commands.command()
    async def fuckthis(self):
        random_quotes = ['Man...',
                         "ARE YOU FUCKING KIDDING ME?!",
                         " ",
                         "well..."]
        await self.bot.say(random.choice(random_quotes) + '\n' + 'https://www.youtube.com/watch?v=5FjWe31S_0g')

    @commands.command()
    async def ayylmao(self):
        ayylmao_repo = [
            'https://goo.gl/MKwbm9',
            'https://goo.gl/gNmzUH',
            'https://goo.gl/rRBVDf'
        ]
        rand = random.choice(range(0, len(ayylmao_repo)))
        await self.bot.say(ayylmao_repo[rand])

    @commands.command()
    async def itsimportant(self):
        await self.bot.say('https://www.youtube.com/watch?v=q6EoRBvdVPQ&list=PL7XlqX4npddfrdpMCxBnNZXg2GFll7t5y')

    @commands.command()
    async def yee(self):
        await self.bot.say('https://youtu.be/q6EoRBvdVPQ')

    @commands.command()
    async def stop(self):
        await self.bot.say('https://www.youtube.com/watch?v=2k0SmqbBIpQ')

    @commands.command()
    async def ping(self):
        await self.bot.say('Pong!')


def setup(bot):
    bot.add_cog(UserUtils(bot))
