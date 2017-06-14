"""
Model for reading CSV format files.
"""

import csv

from src.utilities.InputManager.meta_input_model import Input


class CsvOperator(Input):
    """
    Model for interacting with CSV files.
    """

    def from_stream(self, data):
        """
        Reads and converts the raw data in CSV format provided as a parameter.
        :param data: the data to be parsed
        """

        raise NotImplementedError()

    def from_file(self, file_path):
        """
        Reads a CSV file from a raw text file.
        :param file_path path for the csv file
        """

        csv_rows = []

        with open(file_path, 'r') as csv_file:
            csv_data = csv.reader(csv_file)
            for row in csv_data:
                csv_rows.append(row)

        return csv_rows
