import os, sys
import pickle
import pandas as pd

from books.config.configuration import Configuration
from books.entity.config_entity import DataTransformationConfig, DataValidationConfig
from books.logger import logging
from books.exception import BookException


class DataTransformation:
    def __init__(self, data_transformation_config:DataTransformationConfig, data_validation_config: DataValidationConfig):
        try:
            self.data_transformation_config = data_transformation_config
            self.data_validation_config = data_validation_config
        except Exception as e:
            raise BookException(e, sys) from e 
        
    
    def get_data_transformer_object(self):
        try:
            df = pd.read_csv(self.data_transformation_config.clean_data_path)

            book_pivot = df.pivot_table(columns='user_id', index='title', values= 'rating')
            book_pivot.fillna(0, inplace = True)

            os.makedirs(self.data_transformation_config.transformed_data_dir, exist_ok=True)
            pickle.dump(book_pivot, open(os.path.join(self.data_transformation_config.transformed_data_dir, 'transformed_book_data.pkl'), 'wb'))
            logging.info(f"Saved pivot table data to {self.data_transformation_config.transformed_data_dir}")

            #saving book_names objects for web app in a single file
            book_names = book_pivot.index
            os.makedirs(self.data_validation_config.serialized_objects_dir, exist_ok=True)
            pickle.dump(book_names, open(os.path.join(self.data_validation_config.serialized_objects_dir, 'book_names.pkl'),'wb'))
            logging.info(f"Saving book_names serialization object to {self.data_validation_config.serialized_objects_dir}")
            pickle.dump(book_pivot, open(os.path.join(self.data_validation_config.serialized_objects_dir, 'book_pivot.pkl'),'wb'))
            logging.info(f"Saved book_pivot serialization object to {self.data_validation_config.serialized_objects_dir}")

        except Exception as e:
            raise BookException(e, sys) from e 
        
    
    def initiate_data_transformation(self):
        try:
            self.get_data_transformer_object()
            logging.info(f"{'='*20}Data Transformation log completed.{'='*20} \n\n")
        except Exception as e:
            raise BookException(e, sys) from e 