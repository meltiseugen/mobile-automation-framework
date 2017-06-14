"""
Module that allows access to Platform information.
"""
import json

from settings import Settings


class Platform(object):
    """
    A class that allows access to platform information.
    """

    def __init__(self, platform_type):
        """
        Constructor.
        """
        self.type = platform_type
        self.__config_data = None
        self.__ui_data = None

        with open(Settings.Paths.DEVICE_DATA_PATH) as config_file:
            self.__config_data = json.load(config_file)[self.type]
            config_file.close()

        with open(Settings.Paths.UI_ELEMENTS_PATH) as ui_file:
            self.__ui_data = json.load(ui_file)[self.type]
            ui_file.close()

    def get_details(self):
        """
        Returns the platform configuration details
        :return: returns a dict() with the platform specifications.
        """
        return self.__config_data

    def get_element_xpath(self, element_tag):
        """
        Returns the xpath associated with the element tag as described in the elements file.
        :param element_tag: teh name (tag) of the element.
        :return: returns a app Element.
        """
        try:
            return self.__ui_data[element_tag]
        except KeyError:
            return None
