from pymongo import MongoClient
from datetime import datetime, timedelta

# Replace the following with your MongoDB Atlas connection string
atlas_connection_string = "mongodb+srv://holocubeled:wsp_710m@cluster0.kfh7wn0.mongodb.net/Smart_City?retryWrites=true&w=majority&appName=Cluster0"

# Connect to MongoDB Atlas
client = MongoClient(atlas_connection_string)

# Define the database and collection
db = client['Smart_City']
collection = db['Data_Set']

# Define the timestamp of the last time you fetched data
# For the sake of this example, we'll fetch data from the last 24 hours
last_fetch_time = datetime.now() - timedelta(days=1)

# Query for new entries
new_entries = collection.find({"created_at": {"$gt": last_fetch_time}})

# Process the new entries
for entry in new_entries:
    print(entry)
    # You can add code here to store or use the data locally

# Close the connection
client.close()