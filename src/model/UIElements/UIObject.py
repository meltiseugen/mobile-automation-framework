"""
Module for UIObject class
"""
import time

from src.StaticResources.StaticData import StaticData
from src.model.Exceptions.UIExceptions import NoSuchUIElement


class UIObject(object):
    """
    UIObject definition
    """
    def __init__(self, controller, element_tag=None, xpath=None):
        """
        Constructor.
        :param controller: Main Controller
        :param element_tag: The path of the ui object
        """
        self._element_tag = element_tag
        self._xpath = xpath
        self.__main_controller = controller
        self.__set_element()

    def __set_element(self):
        """

        :return:
        """
        try:
            self._element = self.__main_controller.APPIUM.get_element(self._element_tag)
        except NoSuchUIElement:
            i = 0
            success = False
            while i < StaticData.Errors.RETRY_NUMBER and not success:
                time.sleep(StaticData.Waits.SMALL_SLEEP_TIME)
                try:
                    self._element = self.__main_controller.APPIUM.get_element(self._element_tag)
                    success = True
                    break
                except NoSuchUIElement:
                    pass
                i += 1
            if not success:
                raise NoSuchUIElement()

    def is_visible(self):
        return self._element.is_displayed()

    def is_enabled(self):
        return self._element.is_enabled()

    def get_attribute(self, name):
        """

        :param name:
        :return:
        """
        return self._element.get_attibute(name)
