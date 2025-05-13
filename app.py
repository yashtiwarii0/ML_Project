from src.mlproject.logger import logging
from src.mlproject.exception import CustomException
import sys
from src.mlproject.components.data_ingestion import DataIngestion
from src.mlproject.components.data_transformation import DataTransformation
from src.mlproject.components.data_transformation import DataTransformationConfig
from src.mlproject.components.model_trainer import ModelTrainerConfig , ModelTrainer
import pandas as pd

if __name__ == "__main__":
    logging.info("The execution has started.")
    
    try:
        #data ingestion
        data_ingestion = DataIngestion()
        train_path, test_path = data_ingestion.initiate_data_ingestion()
        logging.info("Data ingestion completed successfully.")
        #data transformation
        data_transformation = DataTransformation()
        test_path, train_path, _ = data_transformation.initiate_data_transormation(train_path, test_path)
        logging.info("Data transformation completed successfully.")
        #model trainer
        model_trainer = ModelTrainer()
        print(model_trainer.initiate_model_trainer(train_path, test_path))
        logging.info("Model training completed successfully.")
        

    except Exception as e:
        logging.error("An error occurred. Raising custom exception.")
        raise CustomException(e, sys)
    