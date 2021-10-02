# gydo.py

A Python Library for interacting with Discord's API

## Example

```py
import gydo

client = gydo.Client("TOKEN")

client.sendMessage("MESSAGE", "CHANNEL_ID")

print(client.user.tag)
```

For now, it currently doesn't interact with Discord's Websocket and only uses Discord's REST API

## Others

`gydo.py` is currently on it's beta stages, so expect it to have some bugs, or if something is incomplete.