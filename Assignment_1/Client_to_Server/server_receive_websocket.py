import asyncio
import websockets

async def echo(websocket, path):
    try:
        async for message in websocket:
            print("Received:", message)
            await websocket.send("Received")
    except websockets.exceptions.ConnectionClosedOK:
        pass
    except Exception as e:
        error_code = str(e.errno) if hasattr(e, "errno") else "UnknownError"
        await websocket.send("Error: " + error_code)

start_server = websockets.serve(echo, "68.183.95.2", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
