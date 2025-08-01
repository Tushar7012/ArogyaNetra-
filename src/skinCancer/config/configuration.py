from skinCancer.constants import CONFIG_FILE_PATH, PARAMS_FILE_PATH
from pathlib import Path
from skinCancer.utils.common import read_yaml, create_directories
from skinCancer.entity.config_entity import DataIngestionConfig,DataValidationConfig

class ConfigurationManager:
    """
    Manages the reading of configuration and parameters to provide
    configuration objects to other components.
    """
    def __init__(
        self,
        config_filepath = CONFIG_FILE_PATH,
        params_filepath = PARAMS_FILE_PATH):

        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)

        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        """
        Reads the data_ingestion configuration from the main config file
        and returns a DataIngestionConfig object.
        """

        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=Path(config.root_dir),
            source_url=config.source_url,
            local_data_file=Path(config.local_data_file)
        )

        return data_ingestion_config
    
    def get_data_validation_config(self) -> DataValidationConfig:
        """
        Reads the data_validation configuration and returns a DataValidationConfig object.
        """
        config = self.config.data_validation
        schema = self.config.data_validation.all_schema

        create_directories([config.root_dir])

        data_validation_config = DataValidationConfig(
            root_dir=Path(config.root_dir),
            STATUS_FILE=config.STATUS_FILE,
            all_schema=schema,
            unzip_data_dir=Path(config.unzip_data_dir)
        )
        return data_validation_config
