

import os
import subprocess
from concurrent.futures import ThreadPoolExecutor

# Define paths and endpoints
tasks = [
    ("sensor_Road1/data.csv", "http://localhost:8000/topic-1"),
    ("sensor_Road2/data.csv", "http://localhost:8000/topic-2"),
    ("sensor_Road3/data.csv", "http://localhost:8000/topic-3"),

]

def run_send_script(file_path, endpoint):
    script_path = os.path.join(os.path.dirname(__file__), 'send.py')
    subprocess.run(["python3", script_path, file_path, endpoint])

# Run tasks concurrently
with ThreadPoolExecutor(max_workers=6) as executor:
    futures = [executor.submit(run_send_script, file_path, endpoint) for file_path, endpoint in tasks]

    for future in futures:
        try:
            future.result()
        except Exception as e:
            print(f"Error: {e}")

