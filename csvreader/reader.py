"""
Module that defines a CSVReader class to read and filter CSV data based
on a given configuration.
"""

import pandas as pd

from .config import Config


class CSVReader:
    """
    A class used to read and filter CSV files.

    Attributes:
        config (dict): Configuration options, including fields to read
        and filters to apply.

    Methods:
        read_data(csv_path: str) -> pd.DataFrame:
            Reads the CSV file located at csv_path, filters it
            based on the specified configuration, and returns a DataFrame.
    """

    def __init__(self, config: Config):
        """
        Initializes the CSVReader with a configuration object.

        Args:
            config (Config): An instance of the Config class containing
            the configuration for reading and filtering the CSV.
        """
        self.config = config.config  # Initialize configuration

    def read_data(self) -> pd.DataFrame:
        """
        Reads and filters data from a CSV file.

        Returns:
            pd.DataFrame: A pandas DataFrame containing the filtered data.

        Raises:
            ValueError: If there is an error reading the CSV file
        """
        csv_path = self.config.get("csv_path", "")  # Get the CSV file path
        # Get the list of fields to read from the configuration
        fields = self.config.get("fields", [])

        try:
            # Read the CSV file with specified columns (fields)
            df = pd.read_csv(csv_path, usecols=fields)
        except pd.errors.EmptyDataError as e:
            # Raise a ValueError if the CSV file is empty
            raise ValueError(f"Error reading CSV file: {e}") from e

        return df  # Return the filtered DataFrame

    def filter_data(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Filters the DataFrame based on the criteria specified in config.

        Args:
            df (pd.DataFrame): The DataFrame to be filtered.

        Returns:
            pd.DataFrame: The filtered DataFrame.
        """
        # Retrieve filter criteria from the configuration
        filters = self.config.get("filters", {})

        # Apply each filter criterion to the DataFrame
        for key, value in filters.items():
            # Filter rows where the value in column 'key' matches the specified 'value'
            df = df[df[key] == value]

        # Return the filtered DataFrame
        return df
