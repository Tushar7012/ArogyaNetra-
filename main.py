from skinCancer.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline
from skinCancer.pipeline.data_validation_pipeline import DataValidationTrainingPipeline

STAGE_NAME = "Data Ingestion stage"

try:
    print(f">>>>>> Stage: {STAGE_NAME} started <<<<<<")
    
    data_ingestion_pipeline = DataIngestionTrainingPipeline()
    data_ingestion_pipeline.main()
    
    print(f">>>>>> Stage: {STAGE_NAME} completed <<<<<<\n\nx==========x")

except Exception as e:
    print(f"An error occurred in {STAGE_NAME}: {e}")
    raise e

STAGE_NAME = "Data Validation stage"
try:
    print(f">>>>>> Stage: {STAGE_NAME} started <<<<<<")
    data_validation_pipeline = DataValidationTrainingPipeline()
    data_validation_pipeline.main()
    print(f">>>>>> Stage: {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    print(f"An error occurred in {STAGE_NAME}: {e}")
    raise e