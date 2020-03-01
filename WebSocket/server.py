import asyncio
import random
import websockets

async def send_message(websocket, path):
    while True:
        message = input()
        # sending the message from input
        await websocket.send(message)
        await asyncio.sleep(random.random() * 5)

start_server = websockets.serve(send_message, "127.0.0.1", 8082)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()