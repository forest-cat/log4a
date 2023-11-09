from shutil import ExecError
from discord.commands import slash_command
from discord.ext import commands
import discord
import json
import os





def read_config():
    os.chdir(os.path.dirname(__file__))
    # Reading Config File
    with open("config.json", "r") as config:
        config = json.load(config)
    return config


config = read_config()

# Defining all variables
PREFIX = "%"
TESTING_GUILD_ID = config["guild_ids"]
TOKEN = config["token"]
DESCRIPTION = """This is a simple Bot to log all actions on a discord server"""
INTENTS = discord.Intents.default()
INTENTS.message_content = True
INTENTS.members = True
INTENTS.presences = True


bot = commands.Bot(command_prefix=PREFIX, description=DESCRIPTION, intents=INTENTS)
bot.remove_command('help')


# Loading the Extensions aka. cogs
registered_extensions = ['cogs.main', 'cogs.events']

for extension in registered_extensions:    
    if extension.startswith('!'):
        print(f"\033[31m[-]\033[00m Extension skipped: {extension.replace('!','')}")
    else:
        bot.load_extension(extension)
        print(f"\033[92m[+]\033[00m Extension loaded: {extension}")
bot.run(TOKEN)