import time
import json
import requests

file_path = './Traffic_Road2_Left.csv'
endpoint = 'http://localhost:8002/producer'

def send_sensor_data(file_path: str, endpoint: str):
    with open(file_path, 'r') as file:
        # Skip the header line
        next(file)
        for index, line in enumerate(file, start=1):
            parts = line.strip().split(',')
            timestamp = parts[0]
            date = parts[1]
            day_of_week = parts[2]
            car_count = int(parts[3])
            bike_count = int(parts[4])
            bus_count = int(parts[5])
            truck_count = int(parts[6])
            total = int(parts[7])
            traffic_situation = parts[8]
            
            data = {
                "index": index,
                "timestamp": timestamp,
                "date": date,
                "day_of_week": day_of_week,
                "car_count": car_count,
                "bike_count": bike_count,
                "bus_count": bus_count,
                "truck_count": truck_count,
                "total": total,
                "traffic_situation": traffic_situation
            }

            json_data = json.dumps(data)

            try:
                response = requests.post(endpoint, json=json_data)
                if response.status_code == 200:
                    print(f"Data {index} sent successfully")
                else:
                    print(f"Failed to send Data {index}. Status code: {response.status_code}")
            except requests.exceptions.RequestException as e:
                print(f"Failed to send Data {index}: {e}")

            time.sleep(30)

send_sensor_data(file_path, endpoint)
