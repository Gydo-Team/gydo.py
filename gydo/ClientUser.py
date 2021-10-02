class ClientUser:
    def __init__(self, rawUser, data, ws):
        self.id = rawUser["id"]
        
        self.discriminator = rawUser["discriminator"]
        
        self.username = rawUser["username"]
        
        self.tag = self.username + '#' + self.discriminator
        
    def get_channel(self, channel_id):
        r = data.manage.RESTGet(ws.channels + channel_id, headers=ws.headers)
        
        return r