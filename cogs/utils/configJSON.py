import ujson

bot_config = {}

try:
    with open("config.json", "r") as jsonFile:
        bot_config = ujson.load(jsonFile)
except FileNotFoundError:
    print("No config file")
    quit(1)

try:
    bot_token = bot_config['bot_token']
except KeyError:
    print("You fool! How am I supposed to work without a token?!")
    quit(1)

try:
    owner_id = bot_config["owner_id"]
except KeyError:
    print("No ID, please, provide a valid ID or some cats will be crying :c")
    quit(1)

try:
    bot_description = bot_config["description"]
except KeyError:
    print("You forgot to add a description, default one will be used")
    bot_description = "Fluffy bot is the most retarded Discord bot and the owner forgot to give me a proper description"

try:
    default_prefix = bot_config["command_prefix"]
except KeyError:
    print("no prefix, default one will be used")
    default_prefix = '//'

try:
    extensions = bot_config["extensions"]
except KeyError:
    print("You have not added any plugins")
    extensions = []

try:
    default_status = bot_config["default_status"]
except KeyError:
    print("No status saved, default will be used")
    default_status = "say " + default_prefix + "help, for help"

try:
    ml_search_link = bot_config["ml_search_link"]
    ml_type = bot_config["ml_type"]
    ml_suffix = bot_config["ml_suffix"]
    ml_account = bot_config["ml_account"]
except Exception:
    print('you have not specified one of the MAL configuration fields')

