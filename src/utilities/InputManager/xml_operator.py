"""
Model for reading XML format files.
"""

from xml.etree import ElementTree as ElemT
from xml.etree.ElementTree import ParseError

import json
import xmltodict


from src.utilities.InputManager.meta_input_model import Input


class XmlOperator(Input):
    """
    Model for interacting with XML files.
    """

    def from_file(self, file_path):
        """
        Reads a XML file from a raw text file.
        :param file_path - path to the xml file to be parsed and returned as a dictionary
        """
        raise NotImplementedError()

    def from_stream(self, data):
        """
        Reads and converts the raw data in XML format provided as a parameter.
        :param data - an xml string to be validated and returned as a dictionary
        """

        try:
            ElemT.fromstring(data)

        except ParseError:
            return None

        return json.loads(json.dumps(xmltodict.parse(data)))
