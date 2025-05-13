import os
import sys
import pymongo
from src.exception import CustomException

class MongoDBClient:
    client = None

    def __init__(self, database_name, ca):
        try:
            mongo_db_url = os.getenv("MONGO_DB_URL")
            if mongo_db_url is None:
                raise Exception("Environment key: MONGO_DB_URL is not set.")
            MongoDBClient.client = pymongo.MongoClient(
                mongo_db_url,
                tlsCAFile=ca,
                ssl=True,
                ssl_cert_reqs='CERT_NONE'
            )
            self.client = MongoDBClient.client
            self.database = self.client[database_name]
            self.database_name = database_name
        except Exception as e:
            lg.error(f"Failed to connect to MongoDB: {str(e)}")
            raise CustomException(f"MongoDB Connection Error: {str(e)}", sys)