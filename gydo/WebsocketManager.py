from restapi import RESTManager
import requests
import platform
import time, json, random
import websockets
import asyncio
import aiohttp
from websockets import connect 

connected = set()

class WebsocketManager:
    def __init__(self, data):
        self.os = platform.system()
        self.token = data.token
        self.wsGateway = 'https://discord.com/api/gateway/bot'
        self.users = data.endpoint + '/users'
        self.channels = data.endpoint + '/channels'
    
    async def connect(self):
        # self.session = aiohttp.ClientSession()
         
        self.headers = {}
        
        self.timeToConnect = 4500 * random.random()
        
        self.defaultWSOpt = {
            "op": 1,
            "d": 2
        }
        
        self.headers['Authorization'] = f'Bot {self.token}'
        self.headers['Content-Type'] = 'application/json'
        
        r = requests.get(self.wsGateway, headers=self.headers)
        
        self.connected = json.dumps(r.text)
        
        self.opGateway = {}
        
        self.opGateway["op"] = 1
        
        self.user_prop = {}
        
        print(self.connected)
        
        async with websockets.connect(f'wss://gateway.discord.gg/?v=9&encoding=json') as ws:
            while True:
                await ws.send(json.dumps(self.defaultWSOpt))
                time.sleep(4.1250)
                
            self.user_prop["op"] = 2
            self.user_prop["d"]['token'] = self.token
            self.user_prop['d']['properties']['$os'] = self.os 
            self.user_prop['d']['properties']['$browser'] = 'my_library'
            self.user_prop['d']['properties']['$device'] = 'my_library'
            
            await ws.send(json.dumps(self.user_prop))
            
            await ws.recv()

        await asyncio.Future()

    def status(self, status):
        # self.opGateway["d"]["status"] = status
        
        print('not yet done wtih status')
        return