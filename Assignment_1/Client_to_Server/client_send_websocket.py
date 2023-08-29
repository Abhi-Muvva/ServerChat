import asyncio
import websockets

async def hello():
    uri = "ws://68.183.95.2:8765"
    async with websockets.connect(uri) as websocket:
        await websocket.send("Hello, Server!")
        response = await websocket.recv()
        print("Received:", response)

asyncio.get_event_loop().run_until_complete(hello())
