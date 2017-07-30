from discord.ext import commands
from framework import utils
from framework.botErrors import BotErrors

opts = {'command_prefix': '//',
        'description': utils.bot_description,
        'command_not_found': ''}

bot = commands.Bot(**opts)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

if __name__ == '__main__':
    for e in utils.extensions:
        bot.load_extension(e)

    bot.run(utils.bot_token)
