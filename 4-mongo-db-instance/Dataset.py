
from pymongo import MongoClient
from datetime import datetime

# Replace the placeholder values with your actual MongoDB Atlas credentials
username = "holocubeled"
password = "wsp_710m"
dbname = "Smart_City"

# Create the connection string
connection_string = f"mongodb+srv://holocubeled:wsp_710m@cluster0.kfh7wn0.mongodb.net/Smart_City?retryWrites=true&w=majority&appName=Cluster0"
# Establish a connection to the MongoDB Atlas cluster
client = MongoClient(connection_string)

# Select the database and collection
db = client['Smart_City']
collection = db['Data_Set']

# Data to be inserted
data = [
    {
        "Time": "12:00:00 AM",
        "Date": 10,
        "DayOfWeek": "Tuesday",
        "CarCount": 31,
        "BikeCount": 0,
        "BusCount": 4,
        "TruckCount": 4,
        "Total": 39,
        "TrafficSituation": "low",
        "created_at": datetime.now()
    },
    {
        "Time": "12:15:00 AM",
        "Date": 10,
        "DayOfWeek": "Tuesday",
        "CarCount": 49,
        "BikeCount": 0,
        "BusCount": 3,
        "TruckCount": 3,
        "Total": 55,
        "TrafficSituation": "low",
        "created_at": datetime.now()
    },
    {
        "Time": "12:30:00 AM",
        "Date": 10,
        "DayOfWeek": "Tuesday",
        "CarCount": 46,
        "BikeCount": 0,
        "BusCount": 3,
        "TruckCount": 6,
        "Total": 55,
        "TrafficSituation": "low",
        "created_at": datetime.now()
    },
    {
        "Time": "12:45:00 AM",
        "Date": 10,
        "DayOfWeek": "Tuesday",
        "CarCount": 51,
        "BikeCount": 0,
        "BusCount": 2,
        "TruckCount": 5,
        "Total": 58,
        "TrafficSituation": "low",
        "created_at": datetime.now()
    },
    {
        "Time": "1:00:00 AM",
        "Date": 10,
        "DayOfWeek": "Tuesday",
        "CarCount": 57,
        "BikeCount": 6,
        "BusCount": 15,
        "TruckCount": 16,
        "Total": 94,
        "TrafficSituation": "normal",
        "created_at": datetime.now()
    },
    {
        "Time": "1:15:00 AM",
        "Date": 10,
        "DayOfWeek": "Tuesday",
        "CarCount": 44,
        "BikeCount": 0,
        "BusCount": 5,
        "TruckCount": 4,
        "Total": 53,
        "TrafficSituation": "low",
        "created_at": datetime.now()
    },
    {
        "Time": "1:30:00 AM",
        "Date": 10,
        "DayOfWeek": "Tuesday",
        "CarCount": 37,
        "BikeCount": 0,
        "BusCount": 1,
        "TruckCount": 4,
        "Total": 42,
        "TrafficSituation": "low",
        "created_at": datetime.now()
    },
    {
        "Time": "1:45:00 AM",
        "Date": 10,
        "DayOfWeek": "Tuesday",
        "CarCount": 42,
        "BikeCount": 4,
        "BusCount": 4,
        "TruckCount": 5,
        "Total": 55,
        "TrafficSituation": "low",
        "created_at": datetime.now()
    },
    {
        "Time": "2:00:00 AM",
        "Date": 10,
        "DayOfWeek": "Tuesday",
        "CarCount": 51,
        "BikeCount": 0,
        "BusCount": 9,
        "TruckCount": 7,
        "Total": 67,
        "TrafficSituation": "low",
        "created_at": datetime.now()
    },
    {
        "Time": "2:15:00 AM",
        "Date": 10,
        "DayOfWeek": "Tuesday",
        "CarCount": 34,
        "BikeCount": 0,
        "BusCount": 4,
        "TruckCount": 7,
        "Total": 45,
        "TrafficSituation": "low",
        "created_at": datetime.now()
    },
    {
        "Time": "2:30:00 AM",
        "Date": 10,
        "DayOfWeek": "Tuesday",
        "CarCount": 45,
        "BikeCount": 0,
        "BusCount": 1,
        "TruckCount": 1,
        "Total": 47,
        "TrafficSituation": "low",
        "created_at": datetime.now()
    }
]

# Insert the data
collection.insert_many(data)

# Close the connection
client.close()