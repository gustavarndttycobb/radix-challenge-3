import threading
import time
import random
from datetime import datetime, timedelta, timezone
import requests

EQUIPMENT_ID = "EQ-12495"
API_URL = "https://httpbin.org/post"
tz_offset = timezone(timedelta(hours=-5))

class SensorWorker:
    def __init__(self):
        self._running = False
        self._thread = None

    def _run(self):
        while self._running:
            data = {
                "equipmentId": EQUIPMENT_ID,
                "timestamp": datetime.now(tz=tz_offset).isoformat(),
                "value": round(random.uniform(50.0, 100.0), 2)
            }
            print("Enviando:", data)
            try:
                response = requests.post(API_URL, json=data)
                print("Status:", response.status_code)
            except Exception as e:
                print("Erro:", e)
            time.sleep(1)

    def start(self):
        if not self._running:
            print("Iniciando sensor...")
            self._running = True
            self._thread = threading.Thread(target=self._run)
            self._thread.start()

    def stop(self):
        if self._running:
            print("Parando sensor...")
            self._running = False
            self._thread.join()
