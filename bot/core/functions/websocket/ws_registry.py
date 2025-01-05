import random
import json
from core.logger.logger import logger
import config
import os
import time

class Client:
    def __init__(self, client_id, websocket, age):
        self.client_id = client_id
        self.websocket = websocket
        self.age = age

    async def send(self, cmd, data=None):
        msg_module = {
            "cmd": cmd,
            "data": data,
            "source": "da_shark"
        }
        await self.websocket.send(json.dumps(msg_module))
        logger.info(f"Sent command to ({self.websocket.remote_address}: {self.client_id}): {cmd}")


class wsRegistry:
    def __init__(self):
        self.clients = {}
        self.address = ""

    def add_client(self, websocket):

                           
        client_id = random.randint(1, 999)
        client = Client(client_id, websocket, time.time())
        for c, v in self.clients.items():
            if v.websocket.remote_address[0] == client.websocket.remote_address[0]:
                self.clients[c] = client
                return self.clients[c]

        self.clients[client_id] = client
        logger.info(f"Client connected: {websocket.remote_address} (CID{client_id})")
        return client

    def remove_client(self, client_id):
        if client_id in self.clients:
            logger.info(f"Client disconnected: {self.clients[client_id].websocket.remote_address} (CID: {client_id})") 
            del self.clients[client_id]
            
    def get_client(self, client_id):
        return self.clients.get(client_id, None)
    
    def fetch_client(self, websocket):
        for client in self.clients.values():
            if client.websocket == websocket:
                return client
        return None

    def all_clients(self):
        return self.clients
    
    def socket_address(self):
        return self.address
    
    def set_address(self, address):
        self.address = address
    
WSRegistry = wsRegistry()    