from collections import namedtuple
from datetime import datetime
import os, sys

from books.logger import logging
from books.exception import BookException
from books.component.data_ingestion import DataIngestion
from books.component.data_validation import DataValidation
from books.config.configuration import Configuration


class Pipeline:
    def __init__(self, config = Configuration()):
        try:
            self.config = config
        except Exception as e:
            raise BookException(e, sys) from e
        
    def start_data_ingestion(self):
        try:
            data_ingestion = DataIngestion(self.config.get_data_ingestion_config())
            return data_ingestion.initiate_data_ingestion()
        except Exception as e:
            raise BookException(e, sys) from e
        
    
    def start_data_validation(self):
        try:
            data_validation = DataValidation(self.config.get_data_validation_config())
            return data_validation.initiate_data_validation()
        except Exception as e:
            raise BookException(e, sys) from e
        

    def run_pipeline(self):
        try:
            data_ingestion = self.start_data_ingestion()
            self.start_data_validation()
        except Exception as e:
            raise BookException(e, sys) from e