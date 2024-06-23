from transfer_all import transfer_all

if __name__ == "__main__":
    topic = "devices/traffic-intersection.test:Sensor_Road1"
    consumer_name = "consumer_0"
    transfer_all(topic, consumer_name)

