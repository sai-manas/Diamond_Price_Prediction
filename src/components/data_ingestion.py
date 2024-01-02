import os
import sys
from src.logger import logging
from src.exception import CustomException
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

## creating the paths by initializing the data ingestion configuration
@dataclass
class DataIngestionConfig:
    raw_path = os.path.join('artifacts','raw.csv')
    train_path = os.path.join('artifacts','train.csv')
    test_path = os.path.join('artifacts','test.csv')


## creating a data ingestion class
class DataIngestion:
    def __init__(self):
        self.config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Data Ingestion method started")

        try:
            df = pd.read_csv(os.path.join('notebooks/data','gemstone.csv'))
            logging.info("Data read as Dataframe using pandas")

            os.makedirs(os.path.dirname(self.config.raw_path), exist_ok=True)
            df.to_csv(self.config.raw_path, index=False)

            train_data,test_data = train_test_split(df, test_size=0.30, random_state=42)
            logging.info("Data got split into train data and test data")

            os.makedirs(os.path.dirname(self.config.train_path), exist_ok=True)
            train_data.to_csv(self.config.train_path, index=False, header=True)

            os.makedirs(os.path.dirname(self.config.test_path), exist_ok=True)
            test_data.to_csv(self.config.test_path, index=False, header=True)

            logging.info("Data ingestion process is completed")

            return(
                self.config.train_path,
                self.config.test_path
            )
        
        except Exception as e:
            logging.info("Error occured in Data Ingestion config")