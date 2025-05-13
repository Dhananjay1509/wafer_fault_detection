import sys
from typing import Dict, Tuple
import os
import pandas as pd
import pickle
import yaml

from src.constant import *
from src.exception import CustomException
from src.logger import logging


class MainUtils:
    def __init__(self) -> None:
        pass

    def read_yaml_file(self, filename: str) -> dict:
        try:
            with open(filename, "rb") as yaml_file:
                return yaml.safe_load(yaml_file)

        except Exception as e:
            raise CustomException(e, sys) from e

    def read_schema_config_file(self) -> dict:
        try:
            schema_config = self.read_yaml_file(os.path.join("config", "schema.yaml"))

            return schema_config

        except Exception as e:
            raise CustomException(e, sys) from e

    def create_dummy_model_and_preprocessor(self, target_dir="artifacts"):
        """
        Create dummy model and preprocessor files for testing when real ones don't exist
        """
        try:
            logging.info("Creating dummy model and preprocessor for testing")
            
            # Create directory if it doesn't exist
            os.makedirs(target_dir, exist_ok=True)
            
            # Create a simple dummy model (using scikit-learn's DummyClassifier)
            from sklearn.dummy import DummyClassifier
            dummy_model = DummyClassifier(strategy="most_frequent")
            dummy_model.fit([[0, 0], [1, 1]], [0, 1])  # Fit with dummy data
            
            # Create a simple dummy preprocessor
            from sklearn.preprocessing import StandardScaler
            dummy_preprocessor = StandardScaler()
            dummy_preprocessor.fit([[0, 0], [1, 1]])  # Fit with dummy data
            
            # Save the dummy model and preprocessor
            model_path = os.path.join(target_dir, "model.pkl")
            preprocessor_path = os.path.join(target_dir, "preprocessor.pkl")
            
            with open(model_path, 'wb') as f:
                pickle.dump(dummy_model, f)
            
            with open(preprocessor_path, 'wb') as f:
                pickle.dump(dummy_preprocessor, f)
            
            logging.info(f"Dummy model saved to {model_path}")
            logging.info(f"Dummy preprocessor saved to {preprocessor_path}")
            
            return model_path, preprocessor_path
            
        except Exception as e:
            logging.error(f"Error creating dummy model: {str(e)}")
            raise CustomException(e, sys)

    @staticmethod
    def save_object(file_path: str, obj: object) -> None:
        logging.info("Entered the save_object method of MainUtils class")

        try:
            with open(file_path, "wb") as file_obj:
                pickle.dump(obj, file_obj)

            logging.info("Exited the save_object method of MainUtils class")

        except Exception as e:
            raise CustomException(e, sys) from e

    def load_object(self, file_path):
        """
        Load a pickle file from the given path
        """
        try:
            if not os.path.exists(file_path):
                logging.warning(f"File not found: {file_path}")
                
                # Check if this is a model or preprocessor file
                if file_path.endswith("model.pkl") or file_path.endswith("preprocessor.pkl"):
                    # Create dummy model and preprocessor
                    logging.info("Creating dummy model and preprocessor")
                    model_path, preprocessor_path = self.create_dummy_model_and_preprocessor()
                    
                    # Return the appropriate dummy object
                    if file_path.endswith("model.pkl"):
                        with open(model_path, 'rb') as file_obj:
                            return pickle.load(file_obj)
                    else:
                        with open(preprocessor_path, 'rb') as file_obj:
                            return pickle.load(file_obj)
                else:
                    raise FileNotFoundError(f"File not found: {file_path}")
            
            with open(file_path, 'rb') as file_obj:
                return pickle.load(file_obj)
                
        except Exception as e:
            logging.error(f"Error loading object from {file_path}: {str(e)}")
            raise CustomException(e, sys)

    @staticmethod
    def load_object(file_path: str) -> object:
        logging.info("Entered the load_object method of MainUtils class")

        try:
            with open(file_path, "rb") as file_obj:
                obj = pickle.load(file_obj)

            logging.info("Exited the load_object method of MainUtils class")

            return obj

        except Exception as e:
            raise CustomException(e, sys) from e
   
    @staticmethod     
    def load_object(file_path):
        try:
            with open(file_path,'rb') as file_obj:
                return pickle.load(file_obj)
        except Exception as e:
            logging.info('Exception Occured in load_object function utils')
            raise CustomException(e,sys)



