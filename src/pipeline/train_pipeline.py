import sys,os

from src.components.data_ingestion import DataIngestion
from src.entity.config_entity import DataIngestionConfig
from src.exception import CustomException
from src.logger import logging
import sys

class TraininingPipeline:
    def __init__(self):
        """
        Initialize the TraininingPipeline with necessary configurations
        """
        # Initialize configuration objects
        self.data_ingestion_config = DataIngestionConfig()
        logging.info("Training pipeline initialized with configurations")

    def start_data_ingestion(self):
        """
        Start the data ingestion process
        """
        try:
            logging.info("Starting data ingestion")
            data_ingestion = DataIngestion(
                data_ingestion_config=self.data_ingestion_config
            )
            feature_store_file_path = data_ingestion.initiate_data_ingestion()
            logging.info(f"Data ingestion completed. Feature store file: {feature_store_file_path}")
            return feature_store_file_path
        except Exception as e:
            logging.error(f"Error in data ingestion: {str(e)}")
            raise CustomException(e, sys)

    def run_pipeline(self):
        """
        Run the complete training pipeline
        """
        try:
            logging.info("Starting training pipeline")
            # Start data ingestion
            feature_store_file_path = self.start_data_ingestion()
            
            # Add other pipeline steps here as needed
            # For example:
            # self.start_data_transformation(feature_store_file_path)
            # self.start_model_trainer()
            
            logging.info("Training pipeline completed successfully")
            return feature_store_file_path
        except Exception as e:
            logging.error(f"Error in training pipeline: {str(e)}")
            raise CustomException(e, sys)


