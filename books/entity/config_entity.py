from collections import namedtuple

TrainingPipelineConfig = namedtuple("TrainingPipelineConfig", ["artifact_dir"])

DataIngestionConfig=namedtuple('DataIngestionConfig', ['dataset_download_url', 'raw_data_dir', 'ingested_dir'])

DataValidationConfig = namedtuple('DataValidationConfig',['books_csv_file', 'ratings_csv_file',
                                                          'clean_data_dir','serialized_objects_dir'])

DataTransformationConfig = namedtuple('DataTransformationConfig', ['clean_data_path', 'transformed_data_dir'])

ModelTrainerConfig = namedtuple('ModelTrainerConfig', ['trained_model_dir', 'trained_model_name','transformed_data_file_dir'])


ModelRecommendationConfig = namedtuple("ModelRecommendationConfig", ["book_name_serialized_objects","book_pivot_serialized_objects",
                                                                    "final_rating_serialized_objects","trained_model_path"])