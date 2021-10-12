import websockets
import aiohttp
import asyncio
import json
import platform

class WebsocketManager:
    """
        Websocket Manager for Discord's WebSocket
    """
    def __init__(self, data):
        self.token = data.token
        self.client = data
        
        self.activity = None
        self.activityType = None
        self.usr = self.user_data

    async def connect(self, connection):
        self.connection = connection
        
        self.identifyBoilerplate = {}
        self.identifyBoilerplate['d'] = {}
        self.identifyBoilerplate['d']['token'] = self.token
                    
        # Indeity Opcode 
        self.identifyBoilerplate['op'] = 2
                    
        # Properties
        self.identifyBoilerplate['d']['properties'] = {
                    '$os': str(platform.system()).lower(),
                    '$browser': 'gydo.py',
                    '$device': 'gydo.py'
                }
                    
        # Intents
        self.identifyBoilerplate['d']['intents'] = 513
                
        await self.connection.send_json(self.identifyBoilerplate)
        
        opHello = await self.connection.receive()
        ack = await self.connection.receive()
        
        usr = await self.connection.receive()
        dump = json.dumps(usr.json())
        res = json.loads(dump)
        usr_data = res

        self.user_data = usr_data
        
        await asyncio.Future()

    async def sendMessage(self, message):
        await self.connection.send_str(message)

    async def heartbeat(self):
        while True:
            try:
                await self.connection.send_str(json.dumps({"op":1,'d':2}))
                await asyncio.sleep(4.1250)
            except KeyboardInterrupt:
                await self.connection.close()
                loop.stop()
    
    async def set_status(self, name):
        self.identifyBoilerplate['d']['presence'] = {}
        self.identifyBoilerplate['d']['presence']['status'] = name
        
        return
