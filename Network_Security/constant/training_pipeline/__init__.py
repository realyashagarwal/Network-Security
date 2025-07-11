import os
import sys
import numpy as np
import pandas as pd


"""
defining common constant variables for the training pipeline
"""
TARGET_COLUMN = "Result"
PIPELINE_NAME: str = "NetworkSecurity"
ARTIFACT_DIR: str = "Artifacts"
FILE_NAME: str = "phishingData.csv"

TRAIN_FILE_NAME: str = "train.csv"
TEST_FILE_NAME: str = "test.csv"


"""
DATA INGESTION RELATED CONSTANTS -> DATA_INGESTION%
"""

DATA_INGESTION_COLLECTION_NAME: str = "phishing data"
DATA_INGESTION_DATABASE_NAME: str = "phishing"
DATA_INGESTION_DIR_NAME: str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"
DATA_INGESTION_INGESTED_DIR: str = "ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO: float = 0.2