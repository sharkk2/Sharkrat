import discord
import config
import traceback
from datetime import datetime
import logging
from colorama import Fore, Style
from core.logger.logger import logger

async def error(interaction: discord.Interaction, bot, e):
    traceback_str = ''.join(traceback.format_exception(type(e), e, e.__traceback__))
    
    embed = discord.Embed(
        title = "Error",
        description = f"Something went wrong\n> Error: `{e}`",
        color = config.embederrorcolor
    )
    
    
    embed.set_author(
        name = interaction.user.display_name if interaction.user.display_name else interaction.user.name,
        icon_url = interaction.user.avatar.url if interaction.user.avatar else interaction.user.default_avatar.url
    )
    
    logger.error(e)
    logging.error(f"{interaction.command.name if interaction.command else 'View'}: {e}")
    await interaction.response.send_message(embed=embed, view=actions(traceback_str, bot, interaction.command, e), ephemeral=True)
    
    
class actions(discord.ui.View):
  def __init__(self, traceback, bot, command, error):
      super().__init__(timeout=None)
      self.traceback = traceback
      self.bot = bot
      self.command = command
      self.error = error
      
  @discord.ui.button(label=f'Report', style=discord.ButtonStyle.red)
  async def fer(self, interaction: discord.Interaction, button: discord.ui.Button):  
      channel = await self.bot.fetch_channel(config.log_channel) 
          
      embed = discord.Embed(title="Error", description=f"Error source: **/ {self.command.qualified_name if self.command else 'Button'}**\n> Guild: **{interaction.guild.name}**\n> Error: `{self.error}`", color=config.embederrorcolor)
      embed.set_author(
          name = f"Reported by {interaction.user.display_name if interaction.user.display_name else interaction.user.name}",
          icon_url = interaction.user.avatar.url if interaction.user.avatar else interaction.user.default_avatar.url
      )
      embed.add_field(name="Traceback", value=f"```{self.traceback}```")
      if channel:
        await channel.send(embed=embed)
        await interaction.response.send_message("Report sent!", ephemeral=True)
        button.disabled = True
        await interaction.message.edit(view=self)
      else:
          await interaction.response.send_message("Report failed to send", ephemeral=True)    
         
  @discord.ui.button(label=f'Full error', style=discord.ButtonStyle.gray)
  async def fe(self, interaction: discord.Interaction, button: discord.ui.Button):  
       try:
            await interaction.response.send_message(embed=discord.Embed(description=f"```{self.traceback[:4060]}...```", color=config.embederrorcolor), ephemeral=True)
       except Exception as e:
          print(e)   
          
          
 