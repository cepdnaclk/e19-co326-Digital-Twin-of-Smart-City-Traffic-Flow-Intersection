# ./sensor_1/app/core/gateways/kafka.py

import asyncio

from aiokafka import AIOKafkaProducer


class Kafka:
    # Class variable to hold the instance of Kafka
    instance = None

    # Constructor method for initializing Kafka instance
    def __init__(
        self,
        topic,
        port,
        servers
    ) -> None:
        # Initialize instance variables
        self._topic = topic
        self._port = port
        self._servers = servers

        # Create a Kafka producer instance and assign it to aioproducer attribute
        self.aioproducer = self.create_kafka()

        # Assign the current instance of Kafka to the class variable instance
        Kafka.instance = self

    # Method to create a Kafka producer
    def create_kafka(self):
        # Get the event loop
        loop = asyncio.get_event_loop()

        # Create and return an instance of AIOKafkaProducer
        return AIOKafkaProducer(
            loop=loop,
            bootstrap_servers=f'{self._servers}:{self._port}'
        )

