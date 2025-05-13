import os
import sys
import pandas as pd
import numpy as np
from pymongo import MongoClient
from src.constant import MONGO_DB_URL, MONGO_DATABASE_NAME, MONGO_COLLECTION_NAME
from src.exception import CustomException
from src.logger import logging
from dataclasses import dataclass
from pathlib import Path

class DataIngestion:
    def __init__(self, data_ingestion_config):
        self.data_ingestion_config = data_ingestion_config
        logging.info("Data Ingestion configuration initialized")

    def export_collection_as_dataframe(self, collection_name=MONGO_COLLECTION_NAME, database_name=MONGO_DATABASE_NAME):
        """
        Export MongoDB collection as a pandas DataFrame
        """
        try:
            logging.info(f"Exporting MongoDB collection: {collection_name} from database: {database_name}")
            
            # Connect to MongoDB
            try:
                import certifi
                ca = certifi.where()
                mongo_client = MongoClient(MONGO_DB_URL, tlsCAFile=ca)
            except ImportError:
                # Connect without certifi if it's not available
                mongo_client = MongoClient(MONGO_DB_URL)
            
            # Get collection
            collection = mongo_client[database_name][collection_name]
            
            # Convert to DataFrame
            df = pd.DataFrame(list(collection.find()))
            
            # Clean up DataFrame
            if "_id" in df.columns.to_list():
                df = df.drop(columns=["_id"], axis=1)
            
            df.replace({"na": np.nan}, inplace=True)
            
            logging.info(f"DataFrame created with shape: {df.shape}")
            return df
            
        except Exception as e:
            logging.error(f"Error in exporting collection as dataframe: {str(e)}")
            raise CustomException(e, sys)
    
    def export_data_into_feature_store_file_path(self):
        """
        Export data from MongoDB to feature store file path
        """
        try:
            logging.info("Exporting data from MongoDB to feature store")
            
            # Get data from MongoDB
            sensor_data = self.export_collection_as_dataframe(
                collection_name=MONGO_COLLECTION_NAME,
                database_name=MONGO_DATABASE_NAME
            )
            
            # Create feature store directory if it doesn't exist
            feature_store_dir = os.path.dirname(self.data_ingestion_config.feature_store_file_path)
            os.makedirs(feature_store_dir, exist_ok=True)
            
            # Save data to feature store
            sensor_data.to_csv(self.data_ingestion_config.feature_store_file_path, index=False)
            
            logging.info(f"Data exported to feature store: {self.data_ingestion_config.feature_store_file_path}")
            return self.data_ingestion_config.feature_store_file_path
            
        except Exception as e:
            logging.error(f"Error in exporting data to feature store: {str(e)}")
            raise CustomException(e, sys)
    
    def initiate_data_ingestion(self) -> Path:
        """
        Initiate the data ingestion process
        """
        logging.info("Initiating data ingestion")
        
        try:
            # Export data to feature store
            feature_store_file_path = self.export_data_into_feature_store_file_path()
            
            logging.info("Data ingestion completed successfully")
            return feature_store_file_path
            
        except Exception as e:
            logging.error(f"Error in data ingestion: {str(e)}")
            raise CustomException(e, sys) from e



