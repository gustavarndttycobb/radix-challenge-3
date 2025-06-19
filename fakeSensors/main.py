import time
import json
from datetime import datetime
import random

EQUIPMENT_ID = "EQ-12495"

def generate_data():
    return {
        "equipmentId": EQUIPMENT_ID,
        "timestamp": datetime.now().astimezone().isoformat(),
        "value": round(random.uniform(50.0, 100.0), 2)
    }

if __name__ == "__main__":
    try:
        while True:
            data = generate_data()
            print(json.dumps(data))
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nEncerrado pelo usuário.")
