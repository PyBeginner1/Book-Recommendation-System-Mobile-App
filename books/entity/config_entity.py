from collections import namedtuple

TrainingPipelineConfig = namedtuple("TrainingPipelineConfig", ["artifact_dir"])

DataIngestionConfig=namedtuple('DataIngestionConfig', ['dataset_download_url', 'raw_data_dir', 'ingested_dir'])

DataValidationConfig = namedtuple('DataValidationConfig',['books_csv_file', 'ratings_csv_file',
                                                          'clean_data_dir','serialized_objects_dir'])

