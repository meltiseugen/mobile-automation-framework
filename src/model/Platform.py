"""
Module that allows access to Platform information.
"""
import json

from src.StaticResources.StaticData import StaticData


class Platform(object):
    """
    A class that allows access to platform information.
    """

    def __init__(self, platform_type):
        """
        Constructor.
        """
        self.type = platform_type
        with open(StaticData.Paths.DEVICE_DATA_PATH) as config_file:
            self.config_data = json.load(config_file)[self.type]
        with open(StaticData.Paths.UI_ELEMENTS_PATH) as ui_file:
            self.ui_data = json.load(ui_file)[self.type]

    def get_details(self):
        return self.config_data

    def get_element_xpath(self, element_tag):
        try:
            return self.ui_data[element_tag]
        except KeyError:
            return None
