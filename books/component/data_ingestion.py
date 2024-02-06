import sys,os
import pandas as pd
import numpy as np
from six.moves import urllib
import zipfile

from books.logger import logging
from books.exception import BookException
from books.config.configuration import Configuration
from books.entity.config_entity import DataIngestionConfig


class DataIngestion:
    def __init__(self, data_ingestion_config: DataIngestionConfig):
        try:
            logging.info(f"{'>>'*20}Data Ingestion log started.{'<<'*20} ")
            self.data_ingestion_config = data_ingestion_config
        except Exception as e:
            raise BookException(e, sys) from e
        
    
    def download_data(self):
        try:
            download_url = self.data_ingestion_config.dataset_download_url
            download_dir = self.data_ingestion_config.raw_data_dir

            os.makedirs(download_dir, exist_ok=True)

            file_name = os.path.basename(download_url)
            file_path = os.path.join(download_dir,file_name)

            logging.info(f"Downloading data from {download_url} into file {file_path}")
            urllib.request.urlretrieve(download_url, file_path)
            logging.info(f"Downloaded data from {download_url} into file {file_path}")
            return file_path
        except Exception as e:
            raise BookException(e, sys) from e
        
    
    def extract_zip_file(self, zip_file_path:str):
        try:
            ingested_dir = self.data_ingestion_config.ingested_dir

            os.makedirs(ingested_dir, exist_ok=True)

            with zipfile.ZipFile(zip_file_path, 'r') as zip:
                zip.extractall(ingested_dir)
            logging.info(f"Extracting zip file: {zip_file_path} into dir: {ingested_dir}")
            ingested_data_path = os.path.join(ingested_dir, os.listdir(ingested_dir)[0])
            return ingested_data_path
        except Exception as e:
            raise BookException(e, sys) from e
        
    
    def initiate_data_ingestion(self):
        try:
            zip_file_path = self.download_data()
            logging.info(f"{'='*20}Data Ingestion log completed.{'='*20} \n\n")
            ingested_data_path = self.extract_zip_file(zip_file_path=zip_file_path)
            return ingested_data_path
        except Exception as e:
            raise BookException(e, sys) from e

    