from src.tr_models.input_model.csv_input import CsvOperator
from src.tr_models.input_model.json_input import JsonOperator
from src.tr_models.input_model.xls_operator import XlsOperator
from src.tr_models.input_model.xml_operator import XmlOperator


class InputModelFactory(object):
    """
    Factory for the Input Model.
    """

    def json_model():
        """
        Returns an instance of the JsonOperator class.
        :return: a reference to a JsonOperator instance.
        """
        return JsonOperator()

    def csv_model():
        """
        Returns an instance of the CsvOperator class.
        :return: a reference to a CsvOperator instance.
        """
        return CsvOperator()

    def xml_model():
        """
        Returns an instance of the XmlOperator class.
        :return: a reference to a XmlOperator instance.
        """
        return XmlOperator()

    def xls_model():
        """
        Returns an instance of the XlsOperator class.
        :param xls_file: xls file to be parsed
        :return:
        """
        return XlsOperator()

    json_model = staticmethod(json_model)
    csv_model = staticmethod(csv_model)
    xml_model = staticmethod(xml_model)
    xls_model = staticmethod(xls_model)