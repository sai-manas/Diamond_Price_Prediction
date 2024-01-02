import os
import sys
from src.logger import logging
from src.exception import CustomException
from src.components.data_ingestion import DataIngestion

if __name__=='__main__':
    obj = DataIngestion()
    train_path,test_path = obj.initiate_data_ingestion()
    print(train_path,test_path)