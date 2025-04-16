from src.mlproject.logger import logging
from src.mlproject.exception import CustomException
import sys
from src.mlproject.components.data_ingestion import DataIngestion
import pandas as pd

if __name__ == "__main__":
    logging.info("The execution has started.")
    
    try:
        data_ingestion = DataIngestion()
        train_path, test_path = data_ingestion.initiate_data_ingestion()

        print("✅ Train CSV Path:", train_path)  # Debug print

        df = pd.read_csv(train_path)
        print("📊 Head of the Train DataFrame:")
        print(df.head())

    except Exception as e:
        logging.error("An error occurred. Raising custom exception.")
        raise CustomException(e, sys)
    