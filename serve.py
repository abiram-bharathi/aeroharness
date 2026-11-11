import os
import asyncio
import websockets
import json

PORT = int(os.environ.get("PORT", 8080))

async def handler(websocket):
    with open("/tmp/smoke_test.txt", "w") as f:
        f.write("AeroHarness smoke test passed.\n")

    async for message in websocket:
        await websocket.send(json.dumps({"type": "done", "status": "completed"}))
        break

async def main():
    async with websockets.serve(handler, "0.0.0.0", PORT):
        print(f"Server listening on 0.0.0.0:{PORT}")
        await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())
