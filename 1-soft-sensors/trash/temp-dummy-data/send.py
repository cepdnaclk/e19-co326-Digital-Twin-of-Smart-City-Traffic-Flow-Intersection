import time
import json
import requests

file_path = './sensor-1-data'
endpoint = 'http://localhost:8000/producer'

def send_sensor_data(file_path: str, endpoint: str):
    with open(file_path, 'r') as file:
        for index, line in enumerate(file, start=1):
            parts = line.split(',')
            timestamp = parts[0].split(': ')[1].strip()
            vehicle_count = int(parts[1].split(': ')[1].strip())

            data = {
                "index": index,
                "timestamp": timestamp,
                "vehicle_count": vehicle_count
            }

            json_data = json.dumps(data)

            try:
                response = requests.post(endpoint, json=data)
                if response.status_code == 200:
                    print(f"Data {index} sent successfully")
                else:
                    print(f"Failed to send Data {index}. Status code: {response.status_code}")
            except requests.exceptions.RequestException as e:
                print(f"Failed to send Data {index}: {e}")

            time.sleep(30)

send_sensor_data(file_path, endpoint)

