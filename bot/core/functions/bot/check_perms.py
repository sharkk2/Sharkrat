import discord
import time
import config



async def check_perms(interaction: discord.Interaction, perms: list, bot, defered: bool = False):
    if all(getattr(interaction.user.guild_permissions, perm, False) for perm in perms) == False:
        perm_list = ", ".join(perms)
        embed = discord.Embed(
            title = "Missing permissions",
            description = f"{config.no} | You can't use this interaction!\n> Missing permissions: `{perm_list}`",
            color = config.embederrorcolor
        )    
        if not defered:
          await interaction.response.send_message(embed = embed, ephemeral = True)
        else:
          msg = await interaction.followup.send(embed = embed, ephemeral = True)  
        return False
    else:
        return True
        
