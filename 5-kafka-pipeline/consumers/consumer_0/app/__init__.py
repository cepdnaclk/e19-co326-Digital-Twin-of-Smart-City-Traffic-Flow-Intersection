# ./consumer_0/app/__init__.py

import logging # for logging msgs
from json import loads # for deserializing json
from app.enum import EnvironmentVariables as EnvVariables # Import the EnvironmentVariables Enum from the app.enum module
from kafka import KafkaConsumer # KafkaConsumer class 
# import csv

def main():
    try:
        # Create a KafkaConsumer instance
        consumer = KafkaConsumer(
            # Specify the topic to consume messages from
            EnvVariables.KAFKA_TOPIC_NAME.get_env(),
            # Specify the bootstrap servers for Kafka
            bootstrap_servers=f'{EnvVariables.KAFKA_SERVER.get_env()}:{EnvVariables.KAFKA_PORT.get_env()}',
            # Specify a function to deserialize message values as JSON
            value_deserializer=lambda x: loads(x.decode('utf-8')),
            # Specify the offset to start consuming messages from
            auto_offset_reset='earliest',
            # Enable auto-committing of offsets
            enable_auto_commit=True,
        )
        '''
        # Open the CSV file in append mode
        with open('consumer_0.csv', 'a', newline='') as csvfile:
            # Create a CSV writer object
            csv_writer = csv.writer(csvfile)
            # Iterate over messages received from the consumer
            for message in consumer:
                # Write the message data to the CSV file
                csv_writer.writerow([message.topic, message.partition, message.offset, message.key, message.value])
         '''       
        # Iterate over messages received from the consumer
        for message in consumer:
            # Print information about the received message
            print("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                                 message.offset, message.key, message.value))
                                                 
    
    # Catch any exception that occurs during execution
    except Exception as e:
        # Log an info message indicating successful connection (this seems incorrect)
        logging.info('Connection successful', e)

# Call the main function when the script is executed
if __name__ == "__main__":
    main()
