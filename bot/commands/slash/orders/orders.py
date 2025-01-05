from discord import app_commands


class orders(app_commands.Group):
      ...
      
  
    
async def setup(bot):
    global Bot 
    Bot = bot 
    bot.tree.add_command(orders(name='commands', description='Remote command orders'))            