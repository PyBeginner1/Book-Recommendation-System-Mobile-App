import os
from datetime import datetime

ROOT_DIR = os.getcwd()

CONFIG_DIR='config'
CONFIG_FILE='config.yaml'
CONFIG_FILE_PATH=os.path.join(ROOT_DIR,CONFIG_DIR,CONFIG_FILE)

def get_current_time_stamp():
    return f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}"

CURRENT_TIME_STAMP = get_current_time_stamp()

# Training pipeline related variable
TRAINING_PIPELINE_CONFIG_KEY = "training_pipeline_config"
TRAINING_PIPELINE_ARTIFACT_DIR_KEY = "artifact_dir"
TRAINING_PIPELINE_NAME_KEY = "pipeline_name"


# Data Ingestion related variable
DATA_INGESTION_CONFIG_KEY = "data_ingestion_config"
DATA_INGESTION_ARTIFACT_DIR = "data_ingestion"
DATA_INGESTION_DOWNLOAD_URL_KEY = "dataset_download_url"
DATA_INGESTION_RAW_DATA_DIR_KEY = "raw_data_dir"
DATA_INGESTION_INGESTED_DIR_NAME_KEY = "ingested_dir"