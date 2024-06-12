import time
import json
import requests
from typing import Optional
from pydantic import BaseModel, ValidationError

file_path = './Traffic_Road1_Right.csv'
endpoint = 'http://localhost:8001/producer'

class Message(BaseModel):
    index: int
    timestamp: str
    date: str
    day_of_week: str
    car_count: int
    bike_count: int
    bus_count: int
    truck_count: int
    total: int
    traffic_situation: str

def send_sensor_data(file_path: str, endpoint: str):
    with open(file_path, 'r') as file:
        # Skip the header line
        next(file)
        for index, line in enumerate(file, start=1):
            parts = line.strip().split(',')
            try:
                message = Message(
                    index=index,
                    timestamp=parts[0],
                    date=parts[1],
                    day_of_week=parts[2],
                    car_count=int(parts[3]),
                    bike_count=int(parts[4]),
                    bus_count=int(parts[5]),
                    truck_count=int(parts[6]),
                    total=int(parts[7]),
                    traffic_situation=parts[8]
                )

                json_data = message.json()
                headers = {'Content-Type': 'application/json'}

                try:
                    response = requests.post(endpoint, data=json_data, headers=headers)
                    if response.status_code == 200:
                        print(f"Data {index} sent successfully")
                    else:
                        print(f"Failed to send Data {index}. Status code: {response.status_code}")
                        print(f"Response content: {response.content}")
                except requests.exceptions.RequestException as e:
                    print(f"Failed to send Data {index}: {e}")

            except ValidationError as e:
                print(f"Validation error for Data {index}: {e}")

            time.sleep(30)
