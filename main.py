from skinCancer.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline

STAGE_NAME = "Data Ingestion stage"

try:
    print(f">>>>>> Stage: {STAGE_NAME} started <<<<<<")
    
    data_ingestion_pipeline = DataIngestionTrainingPipeline()
    data_ingestion_pipeline.main()
    
    print(f">>>>>> Stage: {STAGE_NAME} completed <<<<<<\n\nx==========x")

except Exception as e:
    print(f"An error occurred in {STAGE_NAME}: {e}")
    raise e
