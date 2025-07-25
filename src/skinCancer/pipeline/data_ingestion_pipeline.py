from skinCancer.config.configuration import ConfigurationManager
from skinCancer.components.data_ingestion import DataIngestion

STAGE_NAME = "Data Ingestion Stage"

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        """
        Main function to run the data ingestion pipeline.
        It initializes the configuration and runs the data ingestion component.
        """
        config_manager = ConfigurationManager()
        data_ingestion_config = config_manager.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.initiate_data_ingestion()


if __name__ == '__main__':
    try:
        print(f">>>>>> Stage: {STAGE_NAME} started <<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        print(f">>>>>> Stage: {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        print(f"An error occurred in {STAGE_NAME}: {e}")
        raise e
