from src.MLProject.logger import logging
from src.MLProject.exception import CustomException
import sys
from src.MLProject.components.data_ingestion import DataIngestion
from src.MLProject.components.data_ingestion import DataIngestionConfig




if __name__ == '__main__':
    logging.info('Starting')
    
    
    try:
        #data_ingestion_config=DataIngestionConfig()
        data_ingestion=DataIngestion()
        train_data_path,test_data_path=data_ingestion.initiate_data_ingestion()

        
        
        
        
        
    except Exception as e:
        logging.info("Custom Exception ")
        raise CustomException(e,sys) 