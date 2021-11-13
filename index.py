import bleak
import asyncio

PEBBLE_MAC="4A:77:D7:04:6C:AA"
service = "180D"
char = "00002a37-0000-1000-8000-00805f9b34fb"
import websockets

CLIENTS = set()

async def hr(data1, data2):
    rate = int(data2[1])
    print(rate)
    for client in CLIENTS:
            await client.send(str(rate))
    
    
async def run(loop):
    async with bleak.BleakClient(PEBBLE_MAC, loop=loop, timeout=10) as client:
        await client.get_services()
        await client.start_notify(char,hr)
        print("blah")
        await asyncio.sleep(10000)


async def rec(websocket, path):
    CLIENTS.add(websocket)
    try:
        async for _ in websocket:
            pass
    finally:
        CLIENTS.remove(websocket)

async def run_socket_server():
    async with websockets.serve(rec, "localhost", 5001):
        socket_server = websockets
        await asyncio.Future()  # run forever


async def main():
    # Schedule three calls *concurrently*:
    loop = asyncio.get_event_loop()
    L = await asyncio.gather(
        run_socket_server(),
        run(loop)
    )

asyncio.run(main())
