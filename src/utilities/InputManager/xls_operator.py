"""
Parser for xml files

"""
from pandas import *
from xlrd import open_workbook

from src.tr_models.input_model.meta_input_model import Input


class XlsOperator(Input):
    """

    This class provide xml parsing methods
    """

    def __init__(self):
        pass

    def from_file(self, data):
        """

        :return: all xls rows
        """
        wb = open_workbook(data)
        full_content = []
        for s in wb.sheets():
            for row in range(s.nrows):
                values = []
                for col in range(s.ncols):
                    values.append(s.cell(row, col).value)
                full_content.append(values)
        return full_content

    def from_stream(self, data):
        pass

    @staticmethod
    def to_dict(data):
        """

        convert xls file to dict
        :return:
        """
        xls = ExcelFile(data)
        df = xls.parse(xls.sheet_names[0])
        return df.to_dict()
