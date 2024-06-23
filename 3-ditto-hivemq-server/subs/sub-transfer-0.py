import paho.mqtt.client as mqtt
import requests

# Define MQTT broker address and port
broker = "localhost"  # Change this if your broker is running on a different machine
port = 1883  # Default MQTT port

# Define MQTT topic
topic = "devices/traffic-intersection.test:Sensor_Road1"

# HTTP endpoint URL
endpoint_url = "http://localhost:8000/topic-1"

# Callback function to handle when a message is received
def on_message(client, userdata, message):
    try:
        payload = message.payload.decode()  # Decode message payload
        print(f"Received message '{payload}' on topic '{message.topic}'")

        # Send data to HTTP endpoint
        response = requests.post(endpoint_url, data=payload)
        if response.status_code == 200:
            print("Data sent successfully to endpoint.")
        else:
            print(f"Failed to send data to endpoint. Status code: {response.status_code}")

    except Exception as e:
        print(f"Error sending data to endpoint: {e}")

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

