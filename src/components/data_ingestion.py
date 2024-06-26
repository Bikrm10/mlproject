import os
import sys
from src.exception import CustomException
from src.logger import logging
import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataTransformationConfig


class DataIngestionConfig:
    train_data_path:str = os.path.join('artifact',"train.csv")
    test_data_path:str = os.path.join('artifact',"test.csv")
    raw_data_path:str = os.path.join('artifact',"raw.csv")
class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig() # ingestion_config is initialzed to DataIngestionConfig class which create folder 
    def initiate_data_ingestion(self):
        logging.info("entered the data ingestion method  or component")
        try:
           

            file_path = 'notebook/data/stud.csv'
            if os.path.exists(file_path):
                df = pd.read_csv(file_path)
            else:
                print("File not found:", file_path)
                print("File path:", os.getcwd())



            # loading dataset from folder for now, later this could be any sourcse
            

            logging.info('read the datasets as df')
            #making directory to save the raw data whenever the function is being called
            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path),exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path, index=False,header=True)
            logging.info("train test split initiated")
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)

            # making pipeline to makinf the train set to csv
            train_set.to_csv(self.ingestion_config.train_data_path, index = False, header = True)
            test_set.to_csv(self.ingestion_config.test_data_path, index = False, header = True)

            logging.info("ingestion is completed")
            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )


           
        except Exception as e:
            raise CustomException(e, sys)
if(__name__=="__main__"):
    obj = DataIngestion()
    train_data, test_data = obj.initiate_data_ingestion()

    data_transformation = DataTransformation()
    data_transformation.initiate_data_transformation(train_data,test_data)