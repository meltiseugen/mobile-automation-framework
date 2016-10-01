"""
A file containing the class required to retrieve device application
related information .
"""

import json


class Device:
    """
    The main class used to retrieve application related information about
    the name and location
    of the UI elements.
    """
    def __init__(self, ui_elements_file, device_type):
        """
        Constructor for the class.
        Default path acts as a constant prefix for most of the UI elements'
        exclusive paths.
        :param ui_elements_file: The name of the jackson configuration file that
                                 holds the required information about
                                 the UI elements of the application.
        :param device_type: The name of the operating system that runs on the
                            device, mainly Android or iOS required for
                            retrieving the correct information from the jackson
                            configuration file .
        """
        self.__device_type = device_type
        self.__ui_elements_file = ui_elements_file
        self.__default_path = self.get_default_path()

    def get_available_ui_elements(self):
        """
        Method used to retrieve the NAME of the available UI elements of the application.
        :return: returns the list of available elements.
        """
        with open(self.__ui_elements_file) as json_data_file:
            data = json.load(json_data_file)
        for device in data:
            if device == self.__device_type:
                elements = data[device]
                json_data_file.close()
                return elements

    def get_default_path(self):
        """
        Method used to retrieve the default path that acts as a constant prefix for
        most of the UI elements' exclusive paths.
        :return: returns the string containing the default path.
        """
        with open(self.__ui_elements_file) as json_data_file:
            data = json.load(json_data_file)
        for device in data:
            if device == self.__device_type:
                elements = data[device]
                json_data_file.close()
                return elements["default_path"]

    def get_xpath_of_element(self, name, default_path_override=False):
        """
        Main method used to retrieve the exclusive path of an element given by NAME.
        :param name: The name of the element for which we want to retrieve the
                     exclusive path.
        :param default_path_override: param used to specify the behaviour of the method;
                                      whether to merge the known path with the default path
                                      OR to directly return the path  corresponding to the
                                      name of the element.
        :return: returns a string containing the default path merged with the relative
                     path of the element OR
                 returns a string containing the exclusive path of the element if the
                     default_path_override param is set True.
        """
        ui_elements = self.get_available_ui_elements()
        if name in ui_elements:
            if default_path_override:
                return ui_elements[name]
            else:
                return self.__default_path + ui_elements[name]
        else:
            return None
