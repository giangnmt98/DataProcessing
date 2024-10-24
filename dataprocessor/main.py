"""
This module reads, filters, and processes CSV data based on a given configuration.
"""

import argparse

from config import Config
from processor import DataProcessor

from dataprocessor.utils.custom_logger import CustomLogger


logger = CustomLogger(name="Main").get_logger()

DEFAULT_CONFIG_PATH = "config.yaml"


def load_and_validate_config(config_path: str) -> Config:
    """
    Load and validate the configuration file.

    Args:
        config_path (str): The filesystem path to the configuration file.
    Returns:
        Config: A validated Config object.
    Raises:
        ValueError: If the configuration is invalid.
    """
    config = Config(config_path)
    if not config.validate():
        raise ValueError("Invalid configuration")
    return config


def handle_csv_data(processor: DataProcessor) -> None:
    """
    Process and filter CSV data using the provided DataProcessor.

    Args:
        processor (DataProcessor): An instance of DataProcessor used to
                                   read, filter, and write data.
    """
    data = processor.read_data()
    filtered_data = processor.filter_data(data)
    processor.write_data(filtered_data)
    logger.info("\n%s", str(filtered_data))
    logger.info("Data processing complete.")


def main(config_path: str = DEFAULT_CONFIG_PATH) -> None:
    """
    Main function to orchestrate the processing of CSV data.

    Args:
        config_path (str): Filesystem path to the configuration file.
    """
    config = load_and_validate_config(config_path)
    processor = DataProcessor(config)
    handle_csv_data(processor)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Process CSV data based on a given configuration."
    )
    parser.add_argument(
        "--config_path",
        type=str,
        nargs="?",
        default=DEFAULT_CONFIG_PATH,
        help="Path to the configuration file",
    )
    args = parser.parse_args()
    main(args.config_path)