"""
This module contains test functions for validating the dataprocessor class.
"""

import pandas as pd
from pandas._testing import assert_frame_equal

from dataprocessor.config import Config
from dataprocessor.processor import DataProcessor


class TestPreprocessing:
    """
    TestPreprocessing contains test methods for the DataProcessor class.
    """

    def __init__(self):
        """
        Initializes the TestPreprocessing class with configuration
        and dataprocessor instance.
        """
        self.package_config = None
        self.preprocessing = None

    def setup_method(self):
        """
        Sets up the configuration and dataprocessor instance for each test.
        """
        # Initialize the configuration from the sample YAML file
        self.package_config = Config("dataprocessor/tests/config/sample_config.yaml")
        # Initialize the dataprocessor object with the config
        self.preprocessing = DataProcessor(self.package_config)

    def test_read_data_valid(self):
        """
        Test reading data to ensure it returns the expected DataFrame.

        Raises:
            AssertionError: If the read data does not match the expected DataFrame.
        """
        # Define sample data for testing
        data = {
            "customer_id": [1, 2],
            "first_name": ["Debra", "Kasha"],
            "last_name": ["Burks", "Todd"],
            "phone": ["834234234", "2222222"],
            "email": ["debra.burks@yahoo.com", "kasha.todd@yahoo.com"],
            "city": ["Orchard Park", "Campbell"],
            "state": ["NY", "CA"],
        }
        # Create a DataFrame from the sample data
        df = pd.DataFrame(data)
        # Read data using the preprocessing object
        result_df = self.preprocessing.read_data().toPandas()
        # Assert that the resulting DataFrame matches the expected DataFrame
        assert_frame_equal(df, result_df)

    def test_filter_data_with_filters(self):
        """
        Test filtering data to ensure it applies the correct filters and returns
        the expected DataFrame.

        Raises:
            AssertionError: If the filtered data does not match the expected
                            DataFrame.
        """
        # Define expected data for testing
        expected_data = {
            "customer_id": [1],
            "first_name": ["Debra"],
            "last_name": ["Burks"],
            "phone": ["834234234"],
            "email": ["debra.burks@yahoo.com"],
            "city": ["Orchard Park"],
            "state": ["NY"],
        }
        # Create a DataFrame from the expected data
        expected_df = pd.DataFrame(expected_data)

        # Read raw data using the preprocessing object
        raw_df = self.preprocessing.read_data()

        # Apply filters to the raw DataFrame
        filtered_df = self.preprocessing.filter_data(raw_df).toPandas()

        # Assert that the filtered DataFrame matches the expected DataFrame
        assert_frame_equal(filtered_df, expected_df)

    def test_write_data(self):
        """
        Test writing data to ensure it writes to file correctly and matches the
        input DataFrame.

        Raises:
            AssertionError: If the written data does not match the input
                            DataFrame.
        """
        # Define sample data for testing
        data = {
            "customer_id": [1, 2],
            "first_name": ["Debra", "Kasha"],
            "last_name": ["Burks", "Todd"],
            "state": ["NY", "CA"],
        }
        # Create a DataFrame from the sample data
        df = pd.DataFrame(data)

        # Write data using the preprocessing object
        self.preprocessing.write_data(df)

        # Read the file back and compare it with the input DataFrame
        result_df = pd.read_csv(self.package_config.config.get("output_data_path"))

        # Assert that the final DataFrame matches the DataFrame that was written
        assert_frame_equal(df, result_df)
        # Clean up the output file after the test
        import os

        os.remove(self.package_config.config.get("output_data_path"))
