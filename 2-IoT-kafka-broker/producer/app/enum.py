import os

from enum import Enum

# Define an Enum named EnvironmentVariables which inherits from str and Enum
class EnvironmentVariables(str, Enum):
    # Define Enum members with their corresponding environment variable names
    #KAFKA_TOPIC_NAME = 'KAFKA_TOPIC_NAME'
    KAFKA_SERVER = 'KAFKA_SERVER'
    KAFKA_PORT = 'KAFKA_PORT'

    # Define a method named get_env
    def get_env(self, variable=None):
        # Get the value of the environment variable corresponding to the Enum member
        return os.environ.get(self, variable)

