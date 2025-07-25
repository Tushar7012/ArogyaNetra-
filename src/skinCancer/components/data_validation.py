import os
from pathlib import Path
from skinCancer.entity.config_entity import DataValidationConfig

class DataValidation:
    def __init__(self, config: DataValidationConfig):
        """
        Initializes the DataValidation component.

        Args:
            config (DataValidationConfig): Configuration for data validation.
        """
        self.config = config

    def validate_all_files_exist(self) -> bool:
        """
        Validates that all required directories exist based on the schema.
        Writes the validation status to a file.

        Returns:
            bool: True if all files exist, False otherwise.
        """
        try:
            validation_status = None
            
            all_dirs = list(self.config.all_schema.keys())
            
            data_dir = self.config.unzip_data_dir

            for directory in all_dirs:
                full_path = Path(data_dir) / directory
                if not os.path.isdir(full_path):
                    validation_status = False
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Validation status: {validation_status}")
                    print(f"Validation failed: Directory '{directory}' not found in {data_dir}")
                    return validation_status
            
            validation_status = True
            with open(self.config.STATUS_FILE, 'w') as f:
                f.write(f"Validation status: {validation_status}")
            print("Validation successful: All required directories exist.")
            
            return validation_status

        except Exception as e:
            raise e
