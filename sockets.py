from quart import websocket, Quart
import asyncio
import json
import random
# from comp.obd import LiveData

app = Quart(__name__)

@app.websocket("/speed_live")
async def random_data():
    while True:
        # output = json.dumps(LiveData.speed_live())
        output = json.dumps(random.random() * 100)
        await websocket.send(output)


@app.websocket("/rpm_live")
async def rpmer():
    while True:
        # output = json.dump(LiveData.rpm_live())
        output = json.dumps(random.random() * 7600)
        await websocket.send(output)


@app.websocket("/intake_live")
async def intaker():
    while True:
        # output = json.dump(LiveData.intake_temp_live())
        output = json.dumps(random.random() * 55)
        await websocket.send(output)

if __name__ == "__main__":
    app.run(port=6112)