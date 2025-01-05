
# Wave configuration file



### REQUIRED DATA ###

import discord
import logging
from datetime import datetime


cd = datetime.now().strftime('%Y-%m-%d %I.%M.%S')

### BOT CONFIG ###

WEBSOCKET_PORT = 6969
API_PORT = 4269

local_socket = True
API_AUTH = "SharkIsGigaChad"

version = '1.0.0'

prefix = 's.'

mongouri = ''
dbcollection = "niga"

owner_ids = [1092548532180877415]

main_guild = 123

premium_role = 1234

embedcolor = discord.Color.blurple()

embederrorcolor = discord.Color.red()

name = "um what da sigma"

token = ''

log_channel = 1286392238951239822


### ENV CONFIG ###

directory = 'bot/commands'

edirectory = 'bot/core/events'

tdirectory = 'bot/core/loops'


folder_blacklist = [
    "views",
    "functions",

]

file_blacklist = [
    'registry.py',
    '__init__.py'
]

### STARTUP SETTINGS ###

maintainance = False

log_msgs = True 

log_file = f"debug/boot_{cd}.log"

logging_file_mode = 'w'

logging_level = logging.DEBUG

logging_format = '%(asctime)s - %(levelname)s - %(message)s'

INFO_COLOR = "purple"
ERROR_COLOR = "red"
DEBUG_COLOR = "green"
WARNING_COLOR = "yellow"
FATAL_COLOR = "red2"


# EMOJIS

no = "<:no:1296811045444255755>"
error = "<:no:1296811045444255755>"
tick = "<:tick:1296811053119705118>"
yes = "<:tick:1296811053119705118>"
right = "<:right:1296811051488378930>"
left = "<:left:1296811043531784323>"
reply = "<:reply:1296811047419904091>"
replycont = "<:replycont:1296811049323860020>"


# STATUSES

statuses = [
    {"text": "(g) Guilds", "type": "dnd", "activity": "watching", "url": ""},
    {"text": "(c) Commands", "type": "idle", "activity": "listening", "url": ""},
]

# niga :D
