"""
This module reads, filters, and processes CSV data based on a given configuration.
"""

from csvreader.reader import CSVReader
from csvreader.config import Config

config_path = "config.yaml"  # Define the path to the configuration file

# Create a Config object
config = Config(config_path)

# Create a CSVReader object with the configuration
csv_reader = CSVReader(config)

# Read data from the CSV file
data = csv_reader.read_data()

# Filter the data
filtered_data = csv_reader.filter_data(data)

# Print the filtered data
print(filtered_data)
