import asyncio
import websockets

async def send_messages(websocket, path):
    # messages = ["Hello from server!", "How are you?", "Goodbye!"]
    message = "Hello from server!"
    # for message in messages:
    await websocket.send(message)
    print("Sent:", message)
        # await asyncio.sleep(2)  # Wait for a while before sending the next message

start_server = websockets.serve(send_messages, "68.183.95.2", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
