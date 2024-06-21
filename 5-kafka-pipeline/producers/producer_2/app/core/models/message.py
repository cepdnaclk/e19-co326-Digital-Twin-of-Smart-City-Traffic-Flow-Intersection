from typing import Optional
from pydantic import BaseModel

class Message(BaseModel):
    # Define attributes for the Message class
    # - index: a required attribute of type integer (int)
    # - timestamp: a required attribute of type string (str)
    # - date: a required attribute of type string (str)
    # - day_of_week: a required attribute of type string (str)
    # - car_count: a required attribute of type integer (int)
    # - bike_count: a required attribute of type integer (int)
    # - bus_count: a required attribute of type integer (int)
    # - truck_count: a required attribute of type integer (int)
    # - total: a required attribute of type integer (int)
    # - traffic_situation: a required attribute of type string (str)
    index: int
    timestamp: str
    date: str
    day_of_week: str
    car_count: int
    bike_count: int
    bus_count: int
    truck_count: int
    total: int
    traffic_situation: str

