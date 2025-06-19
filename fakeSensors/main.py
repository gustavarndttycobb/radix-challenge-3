from fastapi import FastAPI
from sensor import SensorWorker

app = FastAPI()
sensor = SensorWorker()

@app.post("/start")
def start_sensor():
    sensor.start()
    return {"status": "sensor started"}

@app.post("/stop")
def stop_sensor():
    sensor.stop()
    return {"status": "sensor stopped"}
