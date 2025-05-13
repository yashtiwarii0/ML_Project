from src.mlproject.logger import logging
from src.mlproject.exception import CustomException
import sys
from src.mlproject.components.data_ingestion import DataIngestion
from src.mlproject.components.data_transformation import DataTransformation
from src.mlproject.components.data_transformation import DataTransformationConfig
import pandas as pd

if __name__ == "__main__":
    logging.info("The execution has started.")
    
    try:
        data_ingestion = DataIngestion()
        train_path, test_path = data_ingestion.initiate_data_ingestion()
        data_tranformation = DataTransformation()
        data_tranformation.initiate_data_transormation(train_path, test_path)
        logging.info("Data transformation completed successfully.")

    except Exception as e:
        logging.error("An error occurred. Raising custom exception.")
        raise CustomException(e, sys)
    