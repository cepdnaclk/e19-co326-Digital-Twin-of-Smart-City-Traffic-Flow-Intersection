## did use before, but currently only uses the send.py in the main dir with concurrent processing

import time
import json
import requests
from typing import Optional
from pydantic import BaseModel, ValidationError


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
                        print(f"Data {index} sent successfully from {file_path}")
                    else:
                        print(f"Failed to send Data {index} from {file_path}. Status code: {response.status_code}")
                        print(f"Response content: {response.content}")
                except requests.exceptions.RequestException as e:
                    print(f"Failed to send Data {index} from {file_path}: {e}")

            except ValidationError as e:
                print(f"Validation error for Data {index} from {file_path}: {e}")

            time.sleep(30)

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: python3 send.py <file_path> <endpoint>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    endpoint = sys.argv[2]
    
    send_sensor_data(file_path, endpoint)

