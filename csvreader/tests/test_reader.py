"""
This module contains test functions for validating the CSVReader class.
"""

import pandas as pd

from csvreader.config import Config
from csvreader.reader import CSVReader


def test_read_data():
    """
    Test the read_data method of CSVReader.

    Ensures that the method reads a CSV file and returns a DataFrame with
    expected properties.

    Raises:
        AssertionError: If any of the assertions are not met.
    """
    config = Config(
        "csvreader/tests/config/sample_config.yaml"
    )  # Initialize Config with a config file
    csv_reader = CSVReader(config)  # Return a CSVReader instance
    data = csv_reader.read_data()  # Read data from CSV file
    assert isinstance(data, pd.DataFrame)  # Check if the result is a DataFrame
    assert len(data) > 0  # Ensure DataFrame is not empty
    assert "last_name" in data.columns  # Verify 'last_name' column exists
