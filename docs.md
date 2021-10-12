# gydo.py Docs

# Table of Contents

- [Classes](#classes)
  - [Client](#client)
  - [Client User / ClientUser](#ClientUser)

## Classes

### Client

For Discord Bot's

**Params:**

`token` - Token of your discord bot

**Example:**

```py
from gydo import Client

client = Client(token)
```

**Functions:**

_Client_.`sendMessage(message, channelId)` - Sending a message manually

### ClientUser

Represents a Discord User

**Params:**

`data` - Data of Main Client
`connection` - Connection to Discord's WebSocket

**Example:**

```py
from gydo import ClientUser

client_user = ClientUser(data)
```