from quart import websocket, Quart
import asyncio
import json
import random
import time
from quart_cors import cors
from comp.obdScan import LiveData

app = Quart(__name__)
app = cors(app)

@app.websocket("/speed_live")
async def random_data():
    while True:
        output = json.dumps(LiveData.speed_live())
        # output = json.dumps(random.random() * 100)
        await websocket.send(output)


@app.websocket("/rpm_live")
async def rpmer():
    while True:
        output = json.dump(LiveData.rpm_live())
        # output = json.dumps(random.random() * 7600)
        await websocket.send(output)


@app.websocket("/intake_live")
async def intaker():
    while True:
        output = json.dump(LiveData.intake_temp_live())
        # output = json.dumps(random.random() * 55)
        await websocket.send(output)

# Fuel data
@app.websocket("/fuel_live")
async def fueler():
    i = 100
    while True:
        output = json.dump(LiveData.fuel_live())
        # i = i - 1
        # output = i
        await websocket.send(json.dumps(output))
        await asyncio.sleep(2)


@app.post("/quit_quart_serv")
def get_out():
    raise Exception("App Now quiting")



if __name__ == "__main__":
    app.run(port=6112)

