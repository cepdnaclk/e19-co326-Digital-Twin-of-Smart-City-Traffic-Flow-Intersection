import paho.mqtt.client as mqtt
import json

# Define MQTT broker address and port
broker = "localhost"  # Change this if your broker is running on a different machine
port = 1883  # Default MQTT port

# Define MQTT topic
topic = "devices/traffic-intersection.test:Sensor_Road1"


# Define message payload
message = {
    "index": 1000,
    "timestamp": "2:30:00 AM",
    "date": "10",
    "day_of_week": "Sunday",
    "car_count": 34,
    "bike_count": 0,
    "bus_count": 4,
    "truck_count": 7,
    "total": 45,
    "traffic_situation": "low",
    "thingId": "traffic-intersection.test:Sensor_Road1"
}

# Convert message to JSON format
payload = json.dumps(message)

# Define MQTT client
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

# Publish message to the topic with QoS level 1
result = client.publish(topic, payload, qos=1)

# Wait for the message to be published
result.wait_for_publish()

# Disconnect from the broker
client.disconnect()
