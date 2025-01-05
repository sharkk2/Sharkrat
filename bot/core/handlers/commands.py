import config
import glob, os
from datetime import datetime
from colorama import Fore, Style
import logging
from core.logger.logger import logger
 
async def register_commands(bot):
    total_commands = 0
    for file_path in glob.iglob(os.path.join(config.directory, '**/*.py'), recursive=True):
        module_path = os.path.relpath(file_path, config.directory)[:-3].replace(os.path.sep, '.')
        if any(folder in module_path.split('.') for folder in config.folder_blacklist):
            continue
        if os.path.basename(file_path) in config.file_blacklist:
            continue
        try:
            await bot.load_extension(f"commands.{module_path}")
            total_commands += 1
            command_name = module_path.split('.')[-1] 
            logger.info(f"Registered {command_name}")
      

        except Exception as e:
            logger.error(f"{e}")
            import traceback
            traceback.print_exc()
            logging.critical(e) 
            
    logger.info(f"Registered all commands ({total_commands})")
    logging.info(f'Registered all commands ({total_commands})')
