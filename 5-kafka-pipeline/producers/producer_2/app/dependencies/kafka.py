# ./real-twin/sensor_1/app/dependencies/kafka.py

from app.core.gateways.kafka import Kafka


def get_kafka_instance():
     # Check if there's already an instance of Kafka created
    if Kafka.instance:
        # If there is, return the existing instance
        return Kafka.instance
    # If no instance exists, create a new instance of Kafka and return it
    return Kafka()

