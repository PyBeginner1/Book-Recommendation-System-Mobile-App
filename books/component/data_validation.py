import os, sys
import pandas as pd
import pickle

from books.logger import logging
from books.exception import BookException
from books.entity.config_entity import DataValidationConfig
from books.config.configuration import Configuration


class DataValidation:
    def __init__(self, data_validation_config:DataValidationConfig):
        try:
            logging.info(f"{'='*20}Data Validation log started.{'='*20} ")
            self.data_validation_config = data_validation_config
        except Exception as e:
            raise BookException(e, sys) from e 
        
    
    def preprocess(self):
        try:
            books = pd.read_csv(self.data_validation_config.books_csv_file, sep =';', encoding='latin-1',on_bad_lines='skip')
            ratings = pd.read_csv(self.data_validation_config.ratings_csv_file, sep =';', encoding='latin-1',on_bad_lines='skip')

            books = books[['ISBN','Book-Title', 'Book-Author', 'Year-Of-Publication', 'Publisher','Image-URL-L']]

            books.rename(columns={"Book-Title":'title',
                                'Book-Author':'author',
                                "Year-Of-Publication":'year',
                                "Publisher":"publisher",
                                "Image-URL-L":"image_url"},inplace=True)

            
            ratings.rename(columns={"User-ID":'user_id',
                                'Book-Rating':'rating'},inplace=True)


            #Users with more than 200 ratings
            x = ratings['user_id'].value_counts() > 200
            y = x[x].index
            ratings = ratings[ratings['user_id'].isin(y)]

            ratings_with_books = ratings.merge(books, on='ISBN')
            number_rating = ratings_with_books.groupby('title')['rating'].count().reset_index()
            number_rating.rename(columns={'rating':'num_of_rating'},inplace=True)
            final_rating = ratings_with_books.merge(number_rating, on='title')

            final_rating = final_rating[final_rating['num_of_rating'] >= 50]

            final_rating.drop_duplicates(['user_id','title'],inplace=True)
            logging.info(f" Shape of the final clean dataset: {final_rating.shape}")
                        
            os.makedirs(self.data_validation_config.clean_data_dir, exist_ok=True)
            final_rating.to_csv(os.path.join(self.data_validation_config.clean_data_dir,'clean_data.csv'), index = False)
            logging.info(f"Saved cleaned data to {self.data_validation_config.clean_data_dir}")

            os.makedirs(self.data_validation_config.serialized_objects_dir, exist_ok=True)
            pickle.dump(final_rating,open(os.path.join(self.data_validation_config.serialized_objects_dir, "final_rating.pkl"),'wb'))
            logging.info(f"Saved final_rating serialization object to {self.data_validation_config.serialized_objects_dir}")

        except Exception as e:
            raise BookException(e, sys) from e 
        
    
    def initiate_data_validation(self):
        try:
            self.preprocess()
            logging.info(f"{'='*20}Data Validation log completed.{'='*20} \n\n")
        except Exception as e:
            raise BookException(e, sys) from e 