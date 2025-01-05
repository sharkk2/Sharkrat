import random
import config
import discord
from core.logger.logger import logger

async def change_status(bot):
    status_data = random.choice(config.statuses)
    
    if 'type' not in status_data:
        return ValueError("No status type found")
    
    type = status_data['type']
    status = None
    if type == 'online':
        status = discord.Status.online
    elif type == 'idle':
        status = discord.Status.idle
    elif type == 'dnd':
        status = discord.Status.dnd
    else:
        status = discord.Status.online
        
    activity = None
    act = status_data['activity']    
    
    total_cmds = 0
    for cmd in bot.tree.walk_commands(): total_cmds += 1
    
    status_data['text'] = status_data['text'].replace('(g)', str(len(bot.guilds)))
    status_data['text'] = status_data['text'].replace('(c)', str(total_cmds))
    
    
    if act == 'playing':
        activity = discord.Activity(type=discord.ActivityType.playing, name=status_data['text'])
    elif act == 'listening':
        activity = discord.Activity(type=discord.ActivityType.listening, name=status_data['text'])
    elif act == 'watching':
        activity = discord.Activity(type=discord.ActivityType.watching, name=status_data['text'])
    elif act == 'streaming':
        activity = discord.Streaming(url=status_data['url'] if 'url' in status_data else 'twitch.tv', name=status_data['text'] if 'text' in status_data else 'Minecraft')
     
        
    await bot.change_presence(status=status, activity=activity)
    #logger.info(f"Status changed to {status_data['text']}")   