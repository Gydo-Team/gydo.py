from restapi import RESTManager
from WebsocketManager import WebsocketManager
import json
from ClientUser import ClientUser
import asyncio

APIEndpoint = 'https://discord.com/api/v8'

class Client:
    def __init__(self, token):
        self.token = token;
        self.endpoint = APIEndpoint
        self.manage = RESTManager(self.token, APIEndpoint)
        
        r = self.manage.RESTGetCurrentUser(self.token, APIEndpoint)
    
        self.ws = WebsocketManager(self)
        
        # asyncio.get_event_loop().run_until_complete(self.ws.connect())
        
        self.data = json.loads(r.text)
        
        self.user = ClientUser(self.data, self, self.ws)
    
    def sendMessage(self, message, channelId, *embed):
        self.messageJSON = {
            'content': f'{message}',
            'embeds': []
        }
        
        r = self.manage.RESTPostMessage(self.token, APIEndpoint, channelId, self.messageJSON)
        
    def MessageEmbed(self, title, description):
        self.MessageEmbedJSON = {
            'title': title,
            'description': description
        }
        
        return self.MessageEmbedJSON
