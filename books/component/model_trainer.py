import os, sys
import pickle
import pandas as pd

from books.logger import logging
from books.exception import BookException
from books.config.configuration import Configuration
from books.entity.config_entity import ModelTrainerConfig


from sklearn.neighbors import NearestNeighbors
from scipy.sparse import csr_matrix



class ModelTrainer:
    def __init__(self, model_trainer_config : ModelTrainerConfig):
        try:
            self.model_trainer_config = model_trainer_config
        except Exception as e:
            raise BookException(e, sys) from e 
        
    
    def trainer(self):
        try:
            # Load the data
            book_pivot = pickle.load(open(self.model_trainer_config.transformed_data_file_dir, 'rb'))
            book_sparse = csr_matrix(book_pivot)

            #Create a model
            model = NearestNeighbors(algorithm='brute')
            # Train the model
            model.fit(book_sparse)

            # Create drirectory to save the trained model
            os.makedirs(self.model_trainer_config.trained_model_dir, exist_ok=True)
            file_path = os.path.join(self.model_trainer_config.trained_model_dir, self.model_trainer_config.trained_model_name)
            # Save the trained model
            pickle.dump(model, open(file_path, 'wb'))
            logging.info(f"Saving final model: [{file_path}]")

        except Exception as e:
            raise BookException(e, sys) from e 
        
    
    def initiate_model_trainer(self):
        try:
            logging.info(f"{'='*20}Model Trainer log started.{'='*20} ")
            self.trainer()
            logging.info(f"{'='*20}Model Trainer log completed.{'='*20} \n\n")
        except Exception as e:
            raise BookException(e, sys) from e 