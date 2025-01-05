# ╔════════════════════╗
# ║                    ║
# ║   © Quantum Labs   ║
# ║                    ║
# ╚════════════════════╝


import discord
from datetime import datetime
from discord.ext import commands
import asyncio
import config
import motor.motor_asyncio
from core.functions.boot.msg_box import msg_box
from core.functions.boot.start import start_bot
from core.functions.boot.sync_db import sync_db
import requests
import logging

from core.logger.logger import logger


# ! FIX AUTO START NON-NRESPONDING BY MAKING IT AUTO START IN BACKGROUND!
# * SIR YES SIR, FIXED!!

prefix = config.prefix
mongouri = config.mongouri

intents = discord.Intents().all()
bot = commands.Bot(command_prefix=prefix, intents=intents, case_insensitive=True)
bot.remove_command('help')

if config.maintainance:  
  logging.basicConfig(
     filename=config.log_file,
     filemode=config.logging_file_mode,
     level=config.logging_level,
     format=config.logging_format,
     datefmt='%Y-%m-%d %I.%M.%S'
  )

    



@bot.event
async def on_ready():
   try:  
     msg_box('\n© Quantum Labs\n')
     await bot.change_presence(status=discord.Status.dnd, activity=discord.Activity(type=discord.ActivityType.playing, name=f"Loading.."))
     bot.start_time = datetime.utcnow()
     
     from core.handlers import commands, events, task_handler      
     from core.functions.bot.error import error
     from core.functions.bot.check_perms import check_perms
     
     bot.error = error 
     bot.check_perms = check_perms
     
     await commands.register_commands(bot) 
     await events.register_events(bot)
     await task_handler.register_tasks(bot)
     logger.info(f"Syncing database")           
     try:
       await sync_db(bot)
       logger.info(f"Database synced successfully")     
     except Exception as e:
       logger.warning(f"Failed to sync database: {e}")
         
      
                                                                                               
     try:
       for view in bot.persistent_views:
         logger.info(f"Refreshed {view.__class__.__name__} '{len(view.children)} item(s)'")
       
       synced = await bot.tree.sync()  
       
       logger.info(f"Synced {len(synced)} command(s)") 
       logging.info(f'Synced {len(synced)} command(s)')
       
       from core.functions.websocket.ws import start as ws_start

       await ws_start(bot)
      
       
     except Exception as e:
       print(e)
       logging.error(e)
     if config.maintainance == True:  
        await bot.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.watching, name=f"Under Maintainance"))
     else:  
        await bot.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.watching, name=f"{len(bot.guilds)} Guilds"))
     
     
   except Exception as e:
       logger.fatal(e)
       logging.critical(e)     


@bot.command()
async def hey(ctx):
  await ctx.send("ayo wsup")

  

async def main():
    async with bot:      
       try:
         bot.mongoConnect = motor.motor_asyncio.AsyncIOMotorClient(config.mongouri)
         
         await start_bot(bot)
         
       except Exception as e:   
         logger.fatal(e)
         logging.critical(e)

if __name__ == "__main__":  
  asyncio.run(main())              
  
# sharkk2