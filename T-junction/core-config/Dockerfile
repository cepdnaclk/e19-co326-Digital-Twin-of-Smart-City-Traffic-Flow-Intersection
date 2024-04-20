# Use the official Kafka Docker image as the base
FROM confluentinc/cp-kafka:latest

# Author
LABEL maintainer="Your Name <your.email@example.com>"

# Set environment variables
ENV KAFKA_VERSION=2.8.0 \
    SCALA_VERSION=2.13 \
    KAFKA_HOME=/opt/kafka \
    PATH=${PATH}:/opt/kafka/bin

# Create directories with appropriate permissions
USER root
RUN mkdir -p /opt/kafka/logs /opt/kafka/data \
    && chown -R 1001:1001 /opt/kafka
USER 1001

# Copy custom configuration files
COPY server.properties /etc/kafka/server.properties

# Expose Kafka port
EXPOSE 9092

# Start Kafka server
CMD ["bash", "-c", "kafka-server-start /etc/kafka/server.properties & sleep infinity"]

