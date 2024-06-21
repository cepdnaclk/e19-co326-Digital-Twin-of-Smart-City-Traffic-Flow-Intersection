# ./real-twin/sensor_1/app/main.py

import time
from app.core.gateways.kafka import Kafka
from app.dependencies.kafka import get_kafka_instance
from app.enum import EnvironmentVariables
from app.routers import publisher
from dotenv import load_dotenv # module to load .env vars
from fastapi import Depends, FastAPI, Request

load_dotenv() # Load environment variables from .env file

app = FastAPI(title='Kafka Publisher API') # Create an instance of FastAPI with a title

# Initialize Kafka server instance with environment variables
kafka_server = Kafka(
    topic=EnvironmentVariables.KAFKA_TOPIC_NAME.get_env(),
    port=EnvironmentVariables.KAFKA_PORT.get_env(),
    servers=EnvironmentVariables.KAFKA_SERVER.get_env(),
)


# Event handler for startup
@app.on_event("startup")
async def startup_event():
    # Start the Kafka producer when the application starts
    await kafka_server.aioproducer.start()
  

# Event handler for shutdown
@app.on_event("shutdown")
async def shutdown_event():
    # Stop the Kafka producer when the application shuts down
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

# Include the router from publisher module with necessary configurations
app.include_router(
    publisher.router,
    prefix="/producer",
    tags=["producer"],
    dependencies=[Depends(get_kafka_instance)],
)

