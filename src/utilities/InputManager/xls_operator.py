"""
Model for reading XLS format files.
"""

from xlrd import open_workbook

from src.utilities.InputManager.meta_input_model import Input


class XlsOperator(Input):
    """
    Model for interacting with XLS files.
    """

    def from_file(self, file_path):
        """
        Reads a XLS file from a raw text file.
        """

        work_book = open_workbook(file_path)
        full_content = []
        for sheet in work_book.sheets():

            for row in range(sheet.nrows):
                values = []
                for col in range(sheet.ncols):
                    values.append(sheet.cell(row, col).value)

                full_content.append(values)

        return full_content

    def from_stream(self, data):
        """
        Reads and converts the raw data in XLS format provided as a parameter.
        """

        raise NotImplementedError()
