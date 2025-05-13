import os
import sys
from src.mlproject.exception import CustomException
from src.mlproject.logger import logging
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
from urllib.parse import quote_plus
import pickle
import numpy as np
load_dotenv()

# Load credentials from .env
host = os.getenv("host")
user = os.getenv("user")
password = os.getenv("password")
db = os.getenv("db")

def read_sql_data(query):
    logging.info("Reading data from SQL database")
    try:
        # Encode special characters in password
        encoded_password = quote_plus(password)

        # Create SQLAlchemy engine
        engine = create_engine(f"mysql+pymysql://{user}:{encoded_password}@{host}/{db}")
        logging.info("Connected to SQL database using SQLAlchemy")
        
        # Execute query and load into DataFrame
        df = pd.read_sql(query, con=engine)
        return df
    except Exception as e:
        raise CustomException(e, sys)

def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)