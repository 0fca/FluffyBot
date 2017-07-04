import ruamel.yaml as yaml
import asyncio

loop = asyncio.get_event_loop()
global_config = {}

# Ensure that the required config.yml file actually exists
try:
    with open("config.yml", "r") as f:
        global_config = yaml.safe_load(f)
except FileNotFoundError:
    print("You have no config file setup! Please use config.yml.sample to setup a valid config file")
    quit()

try:
    bot_token = global_config["bot_token"]
except KeyError:
    print("You have no bot_token saved, this is a requirement for running a bot.")
    print("Please use config.yml.sample to setup a valid config file")
    quit()

try:
    owner_ids = global_config["owner_id"]
except KeyError:
    print("You have no owner_id saved! You're not going to be able to run certain commands without this.")
    print("Please use config.yml.sample to setup a valid config file")
    quit()

# Default bot's description
try:
    bot_description = global_config.get("description")
except Exception:
    print('no description saved')
# Bot's default prefix for commands
try:
    default_prefix = global_config.get("command_prefix", "//")
except Exception:
    print('default command prefix is not specified')

da_secret = global_config.get("da_secret", "")
# The invite link for the server made for the bot
dev_server = global_config.get("dev_server", "")
# The User-Agent that we'll use for most requests
user_agent = global_config.get('user_agent', "")
# The extensions to load
try:
    extensions = global_config.get('extensions', [])
except KeyError:
    print('you have not added any extensions')
# The default status the bot will use
default_status = global_config.get("default_status", None)

#mal section
try:
    ml_search_link = global_config.get("ml_search_link")
    ml_type = global_config.get("ml_type", [])
    ml_suffix = global_config.get("ml_suffix")
    ml_account = global_config.get("ml_account", ())
except Exception:
    print('you have not specified one of the MAL configuration fields')