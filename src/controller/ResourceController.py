"""
Module that handles interactions with various types of files.
"""
import os

from src.model.Exceptions.FileExceptions import NotFound
from src.utilities.InputManager.json_input import JsonOperator
from src.utilities.InputManager.xml_operator import XmlOperator


class ResourceController(object):
    """
    A class that allows interaction with different file types.
    """
    def __init__(self, base_path):
        """
        Initialization
        :param base_path: contains the path to the resources folder
        """
        self.__base_path = base_path

    @staticmethod
    def exists(file_path):
        """
        Returns it the requested file exists or not
        :param file_path: path to file
        :return: boolean
        """
        if os.path.isfile(file_path):
            return True
        raise NotFound(message="File Not Found!")

    @staticmethod
    def get_data(file_path, tags):
        """
        Returns the requested data
        :param file_path: location to the file
        :param tags: the tag path in the file (XML/JSON)
        :return: precious data (String)
        """
        if ResourceController.exists(file_path=file_path):
            if ".json" in file_path:
                data_reader = JsonOperator().from_file(file_path)
                return data_reader.get(tags)
            if ".xml" in file_path:
                data_reader = XmlOperator().from_file(file_path)
                return data_reader.get(tags)
        raise NotFound(message="File not XML or JSON!\nPATH: " + file_path)

    @staticmethod
    def get_files_in_dir(path):
        """
        Returns a list of json and xml files from a given directory.
        :param path: the path to the directory which to scan.
        :return: a list of file names if of type json or xml.
        """
        ret_files = []
        for root, _, files in os.walk(path):
            for file in files:
                if ".json" in file or ".xml" in file:
                    ret_files.append(os.path.join(root, file))
        return ret_files
