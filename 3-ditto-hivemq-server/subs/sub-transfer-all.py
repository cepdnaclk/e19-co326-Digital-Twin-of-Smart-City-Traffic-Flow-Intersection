import threading
import paho.mqtt.client as mqtt
import requests

# Define MQTT broker address and port
broker = "localhost"  # Change this if your broker is running on a different machine
port = 1883  # Default MQTT port

# MQTT topics and HTTP endpoints
configurations = [
    {"topic": "devices/traffic-intersection.test:Sensor_Road1", "endpoint_url": "http://localhost:8000/topic-1"},
    {"topic": "devices/traffic-intersection.test:Sensor_Road2", "endpoint_url": "http://localhost:8000/topic-2"},
    {"topic": "devices/traffic-intersection.test:Sensor_Road3", "endpoint_url": "http://localhost:8000/topic-3"}
]

# Function to handle MQTT client operations
def mqtt_client_thread(topic, endpoint_url):
    def on_message(client, userdata, message):
        try:
            payload = message.payload.decode()  # Decode message payload
            print(f"Received message '{payload}' on topic '{message.topic}'")

            # Send data to HTTP endpoint
            response = requests.post(endpoint_url, data=payload)
            if response.status_code == 200:
                print(f"Data sent successfully to {endpoint_url}.")
            else:
                print(f"Failed to send data to {endpoint_url}. Status code: {response.status_code}")

        except Exception as e:
            print(f"Error sending data to {endpoint_url}: {e}")

    # Define MQTT client
    client = mqtt.Client(client_id="", protocol=mqtt.MQTTv5)

    # Set up logging for debugging
    client.enable_logger()

    # Assign callback function
    client.on_message = on_message

    # Connect to the broker
    client.connect(broker, port, keepalive=60)

    # Subscribe to the topic
    client.subscribe(topic)

    # Loop to maintain connection and process incoming messages
    client.loop_forever()

# Create and start a thread for each configuration
threads = []
for config in configurations:
    thread = threading.Thread(target=mqtt_client_thread, args=(config["topic"], config["endpoint_url"]))
    threads.append(thread)
    thread.start()

# Wait for all threads to complete
for thread in threads:
    thread.join()

