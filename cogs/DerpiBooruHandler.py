import requests


from discord.ext import commands


class DerpiBooru(object):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.search_link = 'https://derpibooru.org/search.json?q='
        self.connection = '+'
        self.respond = ''

    @commands.command(pass_context=True)
    async def dp(self, ctx):
        amount = self.get_amount(ctx.message.content)
        query = self.get_query(ctx.message.content)


    def make_req(self, query):
        pass

    def parse_result(self):
        pass

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
    bot.add_cog(DerpiBooru(bot))
