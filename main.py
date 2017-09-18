import cogs.utils.configJSON as configJson
from discord.ext import commands
import discord

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

@bot.event
async def on_command_error(ctx, error):
    await ctx.send("I'm sorry, something went wrong. This command may not exist")

if __name__ == '__main__':
    for e in configJson.extensions:
        bot.load_extension(e)
    bot.run(configJson.bot_token)