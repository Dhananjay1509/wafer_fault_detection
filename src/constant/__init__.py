import os

# MongoDB configuration
MONGO_DATABASE_NAME = "Dhananjay_DB"
MONGO_COLLECTION_NAME = "waferfault"

TARGET_COLUMN = "quality"

# Get MongoDB URL from environment or use a default for development
MONGO_DB_URL = os.getenv("MONGO_DB_URL")
if not MONGO_DB_URL:
    # For development only - replace with your actual connection string
    MONGO_DB_URL = "mongodb+srv://dhananjay1509:Dhananjay1509@cluster0.omqemyy.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    print("Warning: Using default MongoDB connection. Set MONGO_DB_URL environment variable in production.")

# Add a flag to disable MongoDB in case of connection issues
USE_MONGODB = os.getenv("USE_MONGODB", "true").lower() == "true"

MODEL_FILE_NAME = "model"
MODEL_FILE_EXTENSION = ".pkl"

artifact_folder = "artifacts"






