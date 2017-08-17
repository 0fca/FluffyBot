from discord.ext import commands
import discord
from cogs import utils
import cogs.utils.configJSON as configJson

opts = {'command_prefix': configJson.default_prefix,
        'description': configJson.bot_description,
        'command_not_found': ''}

bot = commands.Bot(**opts)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print(discord.version_info)
    print('------')

@bot.command()
async def foo(ctx, * ,arg: str):
    await ctx.send(arg)

if __name__ == '__main__':
    for e in configJson.extensions:
        bot.load_extension(e)

    bot.run(configJson.bot_token)
