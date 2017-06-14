"""
Model for reading JSON format files.
"""

import json

from src.utilities.InputManager.meta_input_model import Input


class JsonOperator(Input):
    """
    Model for interacting with JSON files.
    """

    def from_file(self, file_path):
        """
        Reads a CSV file from a raw text file.
        :param file_path: path for the json file
        """
        with open(file_path, 'r') as file_descriptor:
            json_data = file_descriptor.read()
            try:
                return json.loads(json_data)

            except ValueError:
                return None

    def from_stream(self, data):
        """
        Reads and converts the raw data in CSV format provided as a parameter.
        :param data: the json data to be validated
        """
        try:
            return json.loads(data)

        except ValueError:
            return None
