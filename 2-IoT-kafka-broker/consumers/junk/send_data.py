import requests
import json
from datetime import datetime

# Define the endpoint and headers
url = "http://localhost:8080/incoming-data"
headers = {
    "Authorization": "Basic ZGV2b3BzOmZvb2Jhcg==",
    "Content-Type": "application/json"
}

# Sample data
data = {
    "index": 10,
    "timestamp": "2:15:00 AM",
    "date": "10",
    "day_of_week": "Tuesday",
    "car_count": 34,
    "bike_count": 0,
    "bus_count": 4,
    "truck_count": 7,
    "total": 45,
    "traffic_situation": "low"
}

# Send data
response = requests.post(url, headers=headers, data=json.dumps(data))

# Print response
print(f"Status Code: {response.status_code}")
print(f"Response: {response.text}")

