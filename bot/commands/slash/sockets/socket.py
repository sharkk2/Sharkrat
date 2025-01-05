from discord import app_commands


class socket(app_commands.Group):
      ...
      
  
    
async def setup(bot):
    global Bot 
    Bot = bot 
    bot.tree.add_command(socket(name='socket', description='Websocket info, control and management'))            