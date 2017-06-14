"""
Factory class for input class models.
"""

from src.utilities.InputManager.csv_input import CsvOperator
from src.utilities.InputManager.json_input import JsonOperator
from src.utilities.InputManager.xml_operator import XmlOperator


class InputModelFactory(object):
    """
    Factory for the Input Model.
    """

    @staticmethod
    def json_model():
        """
        Returns an instance of the JsonOperator class.
        :return: a reference to a JsonOperator instance.
        """
        return JsonOperator()

    @staticmethod
    def csv_model():
        """
        Returns an instance of the CsvOperator class.
        :return: a reference to a CsvOperator instance.
        """
        return CsvOperator()

    @staticmethod
    def xml_model():
        """
        Returns an instance of the XmlOperator class.
        :return: a reference to a XmlOperator instance.
        """
        return XmlOperator()
