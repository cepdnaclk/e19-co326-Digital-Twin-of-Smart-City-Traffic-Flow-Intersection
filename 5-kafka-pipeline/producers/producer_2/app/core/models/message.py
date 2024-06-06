# ./real-twin/sensor_1/app/core/models/message.py

from typing import Optional
from pydantic import BaseModel

class Message(BaseModel):
    # Define three attributes for the Message class: index, timestamp, and vehicle_count
    # - index: a required attribute of type integer (int)
    # - timestamp: a required attribute of type string (str)
    # - vehicle_count: a required attribute of type integer (int)
    index: int
    timestamp: str
    vehicle_count: int
