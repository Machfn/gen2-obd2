from quart import websocket, Quart
import asyncio
import json
import random
from comp.obd import LiveData

app = Quart(__name__)

@app.websocket("/speed_live")
async def random_data():
    while True:
        output = json.dumps(LiveData.speed_live())
        await websocket.send(output)


@app.websocket("/rpm_live")
async def rpmer():
    while True:
        output = json.dump(LiveData.rpm_live())
        await websocket.send(output)


if __name__ == "__main__":
    app.run(port=6112)