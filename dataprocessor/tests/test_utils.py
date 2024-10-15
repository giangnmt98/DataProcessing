"""
This module contains a test function to validate configuration using
`validate_config` function from the `csvreader.utils` module.
"""

from dataprocessor.utils.utils import validate_config


def test_validate_config():
    """
    Test the `validate_config` function to ensure it correctly identifies
    valid and invalid configurations.

    The function defines two configurations:
    - `valid_config`: A dictionary with the required keys and values.
    - `invalid_config`: A dictionary missing the required keys.

    It asserts that:
    - `validate_config(valid_config)` returns `True`.
    - `validate_config(invalid_config)` returns `False`.

    Raises:
        AssertionError: If the `validate_config` function does not return
                        the expected boolean values.
    """

    # Define a valid configuration with the required "fields" key
    valid_config = {"fields": ["last_name", "city"]}

    # Define an invalid configuration without the required "fields" key
    invalid_config = {"invalid_key": "value"}

    # Assert that the valid configuration is recognized as valid
    assert validate_config(valid_config) is True

    # Assert that the invalid configuration is recognized as invalid
    assert validate_config(invalid_config) is False
