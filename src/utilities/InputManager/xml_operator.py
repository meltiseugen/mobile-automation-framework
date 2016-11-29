from src.tr_models.input_model.meta_input_model import Input
import xmltodict
import json
import os
from xml.etree import ElementTree as ET
from xml.etree.ElementTree import ParseError
from ..dictionaries.base_dictionary import BaseDictionary


class XmlOperator(Input):
    def __init__(self):
        pass

    def from_file(self, file_path):
        """
        :param file_path - path to the xml file to be parsed and returned as a dictionary
        """
        try:
            with open(file_path) as fd:
                data = xmltodict.parse(fd.read())
                data = json.loads(json.dumps(data))
                if 'input' in data:
                    return data['input']
                else:
                    contains_list = []  # will contain all the addresses from the xml at the '<address contains/>' tag
                    new_dict = dict()
                    inside_dict = data['validationRules']
                    if 'address' in inside_dict:
                        for address in range(0, len(data['validationRules']['address'])):
                            contains_list.append(data['validationRules']['address'][address]['@contains'])
                    new_dict['address'] = contains_list
                    if 'location' in inside_dict:
                        new_dict['location'] = inside_dict['location']['@near']
                    return new_dict
        except xmltodict.expat.ExpatError:
            return "None"

    def from_stream(self, data):
        """
        :param data - an xml string to be validated and returned as a dictionary
        """
        try:
            ET.fromstring(data)
        except ParseError:
            print("Xml stream not well formed")
            return "None"
        return json.loads(json.dumps(xmltodict.parse(data)))

    def from_folder(self, folder_path, sub_folders):
        """
        :param folder_path - the path to the folder containing xml files
        :param sub_folders - select whether subfolders should be checked or not

        For example: from_folder(path, True) will check the subfolders
                     from_folder(path, False) will not check the subfolders
        """
        xml_array = []
        if sub_folders:
            for file in os.listdir(folder_path):
                if ".xml" in file:
                    xml_array.append(self.from_file(folder_path + file))
        else:
            for subdir, dirs, files in os.walk(folder_path):
                for file in files:
                    if '.xml' in file:
                        xml_array.append(self.from_file(os.path.join(subdir, file)))
        return xml_array
    