import csv

from src.tr_models.input_model.meta_input_model import Input


class CsvOperator(Input):
    def __init__(self):
        pass

    def from_stream(self, data):
        pass

    def from_file(self, file_path):
        """
        :param file_path path for the csv file
        """
        csv_rows = []
        with open(file_path, 'r') as csv_file:
            csv_data = csv.reader(csv_file)
            for row in csv_data:
                csv_rows.append(row)
        return csv_rows
