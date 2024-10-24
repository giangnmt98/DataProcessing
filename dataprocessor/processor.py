"""
Module to process CSV data, including reading, filtering, and writing data.
"""

import pandas as pd

from dataprocessor.config import Config
from dataprocessor.utils.custom_logger import CustomLogger


class DataProcessor:
    """
    A class to process CSV data based on configuration settings.

    Attributes:
        config (dict): Configuration settings for data processing.
    """

    def __init__(self, config: Config):
        """
        Initializes the DataProcessor with the provided configuration.

        Parameters:
            config (Config): An instance of Config containing configuration settings.
        """
        self.config = config.config
        self.logger = CustomLogger(
            name="Data Processing", debug=self.config.get("debug", False)
        ).get_logger()

    def read_data(self) -> pd.DataFrame:
        """
        Reads data from a CSV file based on configuration settings.

        Returns:
            pd.DataFrame: The data read from the CSV file.

        Raises:
            ValueError: If the data cannot be read from the CSV file.
        """
        self.logger.info("Reading data from CSV file.")

        # Get the path to the CSV file from the configuration
        csv_path = self.config.get("input_data_path", "")

        # Get the field definitions from the configuration
        field_definitions = self.config.get("fields", [])

        # Extract field names from the field definitions
        field_names = [list(field.keys())[0] for field in field_definitions]

        # Create a dictionary mapping field names to their data types
        field_types = {
            list(field.keys())[0]: list(field.values())[0]
            for field in field_definitions
        }

        return self.load_csv(csv_path, field_names, field_types)

    @staticmethod
    def convert_data_types(df: pd.DataFrame, field_types: dict) -> pd.DataFrame:
        """
        Converts the data types of DataFrame columns.

        Parameters:
            df (pd.DataFrame): The DataFrame whose column types need to be converted.
            field_types (dict): A dictionary mapping field names to data types.

        Returns:
            pd.DataFrame: The DataFrame with updated data types.
        """
        for field, dtype in field_types.items():
            # Convert the data type of the specified field
            df[field] = df[field].astype(dtype)
        return df

    def load_csv(
        self, csv_path: str, field_names: list, field_types: dict
    ) -> pd.DataFrame:
        """
        Loads data from a CSV file and converts column data types.

        Parameters:
            csv_path (str): The path to the CSV file.
            field_names (list): List of field names to be read from the CSV file.
            field_types (dict): Dictionary mapping field names to data types.

        Returns:
            pd.DataFrame: The loaded and type-converted data.

        Raises:
            ValueError: If an error occurs reading the CSV file.
        """
        try:
            # Read the CSV file into a DataFrame
            df = pd.read_csv(csv_path, usecols=field_names)
            return self.convert_data_types(df, field_types)
        except pd.errors.EmptyDataError as e:
            raise ValueError(f"Error reading CSV file: {e}") from e

    def filter_data(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Filters the DataFrame based on specified criteria in the configuration.

        Parameters:
            df (pd.DataFrame): The DataFrame to be filtered.

        Returns:
            pd.DataFrame: The filtered DataFrame.
        """
        self.logger.info("Filtering data based on criteria.")

        # Get the filter criteria from the configuration
        filter_criteria = self.config.get("filters", {})

        # Apply each filter criterion to the DataFrame
        for key, value in filter_criteria.items():
            df = df[df[key] == value]
        return df

    def write_data(self, data: pd.DataFrame) -> None:
        """
        Writes the data to a CSV file specified in the configuration.

        Parameters:
            data (pd.DataFrame): The DataFrame to be written to a CSV file.

        Raises:
            ValueError: If the output CSV path is not provided
            or an error occurs writing the file.
        """
        self.logger.info("Writing data to CSV file.")

        # Get the output CSV path from the configuration
        output_csv_path = self.config.get("output_data_path")

        if output_csv_path:
            try:
                # Write the DataFrame to the CSV file
                data.to_csv(output_csv_path, index=False)
            except Exception as e:
                raise ValueError(f"Error writing CSV file: {e}") from e
        else:
            raise ValueError("Output CSV path not provided in configuration.")
