import os,sys

from books.logger import logging
from books.exception import BookException
from books.constant import *
from books.util.util import read_yaml_file
from books.entity.config_entity import DataIngestionConfig, TrainingPipelineConfig


class Configuration:
    def __init__(self, config_file_path: str=CONFIG_FILE_PATH, time_stamp:str = CURRENT_TIME_STAMP):
        try:
            self.config_info = read_yaml_file(config_file_path)
            logging.error(self.config_info)
            self.time_stamp = time_stamp
            self.training_pipeline_config=self.get_training_pipeline_config()

        except Exception as e:
            raise BookException(e, sys) from e
        
    
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        try:
            artifact_dir = self.training_pipeline_config.artifact_dir

            data_ingestion_config_info = self.config_info[DATA_INGESTION_CONFIG_KEY]

            dataset_download_url = data_ingestion_config_info['dataset_download_url']

            raw_data_dir = os.path.join(artifact_dir, data_ingestion_config_info['raw_data_dir'])

            ingested_dir = os.path.join(artifact_dir, data_ingestion_config_info['ingested_dir'])

            data_ingestion_config = DataIngestionConfig(dataset_download_url=dataset_download_url,
                                                        raw_data_dir=raw_data_dir,
                                                        ingested_dir=ingested_dir)
            
            logging.info(f'Data Ingestion Config: {data_ingestion_config}')
            return data_ingestion_config
        except Exception as e:
            raise BookException(e, sys) from e
        

    def get_training_pipeline_config(self) -> TrainingPipelineConfig:
        try:
            training_pipeline_config_info = self.config_info['training_pipeline_config']
            artifact_dir = os.path.join(ROOT_DIR, training_pipeline_config_info['pipeline_name'],
                                                    training_pipeline_config_info['artifact_dir'])
            training_pipeline_config = TrainingPipelineConfig(artifact_dir=artifact_dir)
            
            logging.info(f'Training pipeline config: {training_pipeline_config}')
            return training_pipeline_config
        except Exception as e:
            raise BookException(e, sys) from e
            