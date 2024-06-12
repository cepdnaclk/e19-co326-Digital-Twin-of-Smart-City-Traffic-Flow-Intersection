# Set python version
ARG BASE_CONTAINER=python:3.8

# Set the base image 
FROM --platform=linux/amd64 $BASE_CONTAINER

# Install pip and requests
RUN apt-get update && apt-get install -y python3-pip && \
    pip3 install --no-cache-dir requests

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Run send.py when the container launches
CMD ["python3", "send.py"]

