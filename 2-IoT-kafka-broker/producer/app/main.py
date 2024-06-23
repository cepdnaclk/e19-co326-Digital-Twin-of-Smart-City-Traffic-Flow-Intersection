# ./real-twin/sensor_1/app/main.py

import time
from app.core.gateways.kafka import Kafka
from app.dependencies.kafka import get_kafka_instance
from app.enum import EnvironmentVariables
from app.routers import publisher_topic1
from app.routers import publisher_topic2
from app.routers import publisher_topic3
from dotenv import load_dotenv # module to load .env vars
from fastapi import Depends, FastAPI, Request
import asyncio
from aiokafka.errors import KafkaConnectionError

load_dotenv() # Load environment variables from .env file

app = FastAPI(title='Kafka Publisher API') # Create an instance of FastAPI with a title

# Initialize Kafka server instance with environment variables
'''
kafka_server = Kafka(
    topic=EnvironmentVariables.KAFKA_TOPIC_NAME.get_env(),
    port=EnvironmentVariables.KAFKA_PORT.get_env(),
    servers=EnvironmentVariables.KAFKA_SERVER.get_env(),
)
'''
# Initialize Kafka server instances for each topic
kafka_servers = {
    "Sensor_Road1": Kafka(
        topic="Sensor_Road1",
        port=EnvironmentVariables.KAFKA_PORT.get_env(),
        servers=EnvironmentVariables.KAFKA_SERVER.get_env()
    ),
    "Sensor_Road2": Kafka(
        topic="Sensor_Road2",
        port=EnvironmentVariables.KAFKA_PORT.get_env(),
        servers=EnvironmentVariables.KAFKA_SERVER.get_env()
    ),
    "Sensor_Road3": Kafka(
        topic="Sensor_Road3",
        port=EnvironmentVariables.KAFKA_PORT.get_env(),
        servers=EnvironmentVariables.KAFKA_SERVER.get_env()
    ),
}


async def start_kafka_producer_with_retry(kafka_server):
    retries = 5
    for attempt in range(retries):
        try:
            await kafka_server.aioproducer.start()
            return
        except KafkaConnectionError as e:
            if attempt < retries - 1:
                print(f"Kafka connection failed, retrying in 5 seconds... ({attempt+1}/{retries})")
                await asyncio.sleep(5)
            else:
                raise e

@app.on_event("startup")
async def startup_event():
    for kafka_server in kafka_servers.values():
        await start_kafka_producer_with_retry(kafka_server)

@app.on_event("shutdown")
async def shutdown_event():
    for kafka_server in kafka_servers.values():
        await kafka_server.aioproducer.stop()
        

# Middleware to add process time header to responses
@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    # Record the start time
    start_time = time.time()
    
    # Call the next middleware or the request handler
    response = await call_next(request)
    
    # Calculate the process time
    process_time = time.time() - start_time
    
    # Add the process time as a response header
    response.headers["X-Process-Time"] = str(process_time)
    
    return response

# Route handler for the root endpoint
@app.get('/')
def get_root():
    return {'message': 'API is running...'}

'''
# Include the router from publisher module with necessary configurations
app.include_router(
    publisher.router,
    prefix="/producer",
    tags=["producer"],
    dependencies=[Depends(get_kafka_instance)],
)

'''

# Include routers for each topic
app.include_router(
    publisher_topic1.router,
    prefix="/topic-1",
    tags=["topic-1"]
)

app.include_router(
    publisher_topic2.router,
    prefix="/topic-2",
    tags=["topic-2"]
)

app.include_router(
    publisher_topic3.router,
    prefix="/topic-3",
    tags=["topic-3"]
)



