import config
import glob, os
from datetime import datetime
from colorama import Fore, Style
import logging  
from core.logger.logger import logger
  
  
async def register_tasks(bot):
    total_loops = 0
    for file_path in glob.iglob(os.path.join(config.tdirectory, '**/*.py'), recursive=True):
        module_path = os.path.relpath(file_path, config.tdirectory)[:-3].replace(os.path.sep, '.')
        if any(folder in module_path.split('.') for folder in config.folder_blacklist):
            continue
        if os.path.basename(file_path) in config.file_blacklist:
            continue
        try:
            await bot.load_extension(f"core.loops.{module_path}")
            total_loops += 1
            task_name = module_path.split('.')[-1] 
            logger.info(f"Registered {task_name}")
        except Exception as e:
            logger.fatal(e)        
            logging.critical(e)
    logger.info(f"Registered all loops ({total_loops})")
    logging.info(f'Registered all task loops ({total_loops})')