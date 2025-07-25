from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    """
    Configuration entity for the data ingestion component.
    
    Attributes:
        root_dir (Path): The root directory where the data ingestion artifacts will be stored.
        source_url (str): The URL of the website to scrape for images.
        local_data_file (Path): The path to the local directory where scraped images will be saved.
    """
    root_dir: Path
    source_url: str
    local_data_file: Path


@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    STATUS_FILE: str
    all_schema: dict # Using 'dict' for flexibility with YAML schema
    unzip_data_dir: Path