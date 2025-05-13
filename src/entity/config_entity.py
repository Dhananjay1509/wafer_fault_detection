import os
from dataclasses import dataclass
from datetime import datetime
from src.constant import artifact_folder

@dataclass
class DataIngestionConfig:
    def __init__(self):
        # Create timestamp for unique artifact folders
        self.timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        
        # Define artifact folder structure
        self.artifact_folder = os.path.join(artifact_folder, self.timestamp)
        self.feature_store_file_path = os.path.join(
            self.artifact_folder, "feature_store", "sensor_data.csv"
        )
        
        # Create directories
        os.makedirs(os.path.dirname(self.feature_store_file_path), exist_ok=True)