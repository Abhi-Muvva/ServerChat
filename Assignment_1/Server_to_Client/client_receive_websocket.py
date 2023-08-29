import asyncio
import websockets

async def receive_messages():
    uri = "ws://68.183.95.2:8765"
    async with websockets.connect(uri) as websocket:
        while True:
            message = await websocket.recv()
            print("Received:", message)
            await websocket.send("Received")

asyncio.get_event_loop().run_until_complete(receive_messages())
