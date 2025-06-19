import time
import json
import random
from datetime import datetime, timedelta, timezone
import requests

EQUIPMENT_ID = "EQ-12495"
API_URL = "https://httpbin.org/post"  # Pode substituir por sua URL real

# Forçar timezone -05:00
tz_offset = timezone(timedelta(hours=-5))

def generate_data():
    return {
        "equipmentId": EQUIPMENT_ID,
        "timestamp": datetime.now(tz=tz_offset).isoformat(),
        "value": round(random.uniform(50.0, 100.0), 2)
    }

if __name__ == "__main__":
    try:
        while True:
            data = generate_data()
            print("Enviando:", data)
            
            response = requests.post(API_URL, json=data)
            print("Status:", response.status_code)
            print("Resposta:", response.json())

            time.sleep(1)
    except KeyboardInterrupt:
        print("\nEncerrado pelo usuário.")
