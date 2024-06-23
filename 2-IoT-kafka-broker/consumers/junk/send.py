import requests
import os

def send_data(file_path, endpoint):
    headers = {
        "content-type": "application/json",  # Adjust content-type as per your data format
        "Authorization": "Basic ZGV2b3BzOmZvb2Jhcg=="
        }

    with open(file_path, 'rb') as file:
        data = file.read()

    try:
        response = requests.post(endpoint, headers=headers, data=data)
        response.raise_for_status()
        print(f"Data sent successfully to {endpoint}")
    except requests.exceptions.RequestException as e:
        print(f"Error sending data to {endpoint}: {e}")

if __name__ == "__main__":
    tasks = [
        ("sensor_Road1/data.csv", "http://localhost:8080/ditto-event/org.eclipse.ditto:dfe57be6-636f-4a11-ba4e-0fc6e522ff95"),
        ("sensor_Road2/data.csv", "http://localhost:8080/ditto-event/org.eclipse.ditto:dfe57be6-636f-4a11-ba4e-0fc6e522ff95"),
        ("sensor_Road3/data.csv", "http://localhost:8080/ditto-event/org.eclipse.ditto:dfe57be6-636f-4a11-ba4e-0fc6e522ff95"),
    ]

    for file_path, endpoint in tasks:
        send_data(file_path, endpoint)

