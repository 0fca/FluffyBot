from discord.ext import commands
import discord
from cogs import utils

opts = {'command_prefix': '//',
        'description': utils.bot_description,
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
    for e in utils.extensions:
        bot.load_extension(e)

    bot.run(utils.bot_token)
