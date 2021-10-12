import asyncio
import pymitter
import json

class ClientUser:
    def __init__(self, client):
        self.id = None 
        
        self.discriminator = None 
        
        self.username = None
    
        self.tag = None