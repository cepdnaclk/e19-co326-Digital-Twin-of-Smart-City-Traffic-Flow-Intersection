# ./real-twin/sensor_1/app/routers/publisher.py

import json
from app.core.gateways.kafka import Kafka
from app.core.models.message import Message
from app.dependencies.kafka import get_kafka_instance
from fastapi import APIRouter, Depends


# Create an instance of APIRouter
router = APIRouter()

# Define a route for handling POST requests
@router.post("/")
# Define the function send that takes a Message object as data and a Kafka object as server
async def send(data: Message, server: Kafka = Depends(get_kafka_instance)):
    try:
        # Get the topic name from the Kafka instance
        topic_name = server._topic
        
        # Convert the Message object to a JSON string and encode it to ASCII
        message_json = json.dumps(data.dict()).encode("ascii")
        
        # Send the message to the Kafka server and wait for acknowledgment
        await server.aioproducer.send_and_wait(topic_name, message_json)
    
    # If any exception occurs
    except Exception as e:
        # Stop the Kafka producer
        await server.aioproducer.stop()
        
        # Raise the caught exception
        raise e
    
    # If the message is sent successfully, return a success message
    return 'Message sent successfully'

