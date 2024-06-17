import os
import subprocess
from concurrent.futures import ThreadPoolExecutor

# Define paths and endpoints
tasks = [
    ("sensor_Road1_Left/data.csv", "http://localhost:8000/producer"),
    ("sensor_Road1_Right/data.csv", "http://localhost:8001/producer"),
    ("sensor_Road2_Left/data.csv", "http://localhost:8002/producer"),
    ("sensor_Road2_Right/data.csv", "http://localhost:8003/producer"),
    ("sensor_Road3_Left/data.csv", "http://localhost:8004/producer"),
    ("sensor_Road3_Right/data.csv", "http://localhost:8005/producer")

]

def run_send_script(file_path, endpoint):
    script_path = os.path.join(os.path.dirname(__file__), 'send.py')
    subprocess.run(["python", script_path, file_path, endpoint])

# Run tasks concurrently
with ThreadPoolExecutor(max_workers=6) as executor:
    futures = [executor.submit(run_send_script, file_path, endpoint) for file_path, endpoint in tasks]

    for future in futures:
        try:
            future.result()
        except Exception as e:
            print(f"Error: {e}")

