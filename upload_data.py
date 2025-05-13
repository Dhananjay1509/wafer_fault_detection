from pymongo.mongo_client import MongoClient
import pandas as pd
import json
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get MongoDB connection string from environment variable
uri = os.getenv("MONGO_DB_URL")
if not uri:
    raise ValueError("MONGO_DB_URL environment variable is not set. Please set it in your .env file.")

# Create a new client and connect to the server
client = MongoClient(uri)

# Database configuration - also use environment variables if possible
DATABASE_NAME = os.getenv("MONGO_DATABASE_NAME", "Dhananjay_DB")
COLLECTION_NAME = os.getenv("MONGO_COLLECTION_NAME", "waferfault")

# read the data as a dataframe
df = pd.read_csv(r"C:\Users\15dha\OneDrive\Desktop\Sensor project\notebooks\wafer_23012020_041211.csv")
df = df.drop("Unnamed: 0", axis=1)

# Convert the data into json
json_record = list(json.loads(df.T.to_json()).values())

# now dump the data into the database
client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)

print(f"Successfully uploaded data to {DATABASE_NAME}.{COLLECTION_NAME}")

