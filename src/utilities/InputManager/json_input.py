import json
from .meta_input_model import Input


class JsonOperator(Input):
    def __init__(self):
        pass

    def from_file(self, file_path):
        """
        :param file_path: path for the json file
        """
        with open(file_path, 'r') as f:
            json_data = f.read()
            try:
                return json.loads(json_data)
            except ValueError:
                print("Not a valid Json")
                return "None"

    def from_stream(self, json_data):
        """
        :param json_data: the json data to be validated
        """
        try:
            return json.loads(json_data)
        except ValueError:
            print("Not a valid Json")
            return "None"
