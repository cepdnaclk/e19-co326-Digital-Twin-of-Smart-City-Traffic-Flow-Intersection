import paho.mqtt.client as mqtt
import json
import subprocess
import time
import sys

def transfer_all(topic, consumer_name):
    # Define MQTT broker address and port
    broker = "localhost"  # Change this if your broker is running on a different machine
    port = 1883  # Default MQTT port

    # Define MQTT client for MQTTv5
    client = mqtt.Client(client_id="", protocol=mqtt.MQTTv5)

    # Set up logging for debugging
    client.enable_logger()

    # Define the on_connect and on_publish callbacks
    def on_connect(client, userdata, flags, rc):
        print(f"Connected with result code {rc}")

    def on_publish(client, userdata, mid):
        print(f"Message {mid} published.")

    client.on_connect = on_connect
    client.on_publish = on_publish

    # Connect to the broker
    client.connect(broker, port, keepalive=60)

    # Function to extract JSON data from the logs
    def extract_json_from_logs(log_line):
        try:
            # Locate the start of the JSON string
            start_index = log_line.find("value=")
            if start_index == -1:
                raise ValueError("Invalid log line format")

            # Extract and clean up the JSON string
            json_str = log_line[start_index + len("value="):].strip()
            
            # Replace single quotes with double quotes to make it valid JSON
            json_str = json_str.replace("'", "\"")
            
            # Convert to Python dictionary
            json_data = json.loads(json_str)
            return json_data
        except (ValueError, json.JSONDecodeError) as e:
            print(f"Failed to parse JSON from log line: {log_line}")
            print(f"Error: {e}")
            return None
        except KeyboardInterrupt:
            print("Exiting...")
            client.disconnect()  # Disconnect MQTT client on exit
            sys.exit(0)

    # Continuously read Docker logs and publish messages
    while True:
        try:
            # Read Docker logs
            logs = subprocess.check_output([ "docker", "logs", "--tail", "1", consumer_name]).decode("utf-8")
            log_lines = logs.strip().split("\n")
            
            for log_line in log_lines:
                message = extract_json_from_logs(log_line)
                if message:
                    payload = json.dumps(message)
                    result = client.publish(topic, payload, qos=1)
                    result.wait_for_publish()
            
            time.sleep(10)  # Wait for 10 sec before reading logs again

        except subprocess.CalledProcessError as e:
            print(f"Failed to read Docker logs: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")

    # Disconnect from the broker
    client.disconnect()

