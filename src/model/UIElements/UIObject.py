"""
Module for UIObject class.
"""

import time

from settings import Settings
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
        self._element = None

    def _set_element(self):
        """
        Creates the link between the class and the UI element.
        Virtualizes the UI element.
        """

        try:
            self._element = self.__main_controller.appium.get_element(self._element_tag)
        except NoSuchUIElement:
            # TODO : you know what!
            index_ = 0
            success = False
            while index_ < Settings.Errors.RETRY_NUMBER and not success:
                time.sleep(Settings.Waits.SMALL_SLEEP_TIME)
                try:
                    self._element = self.__main_controller.appium.get_element(self._element_tag)
                    success = True
                    break

                except NoSuchUIElement:
                    pass

                index_ += 1

            if not success:
                raise NoSuchUIElement()

    def is_visible(self):
        """
        Checks if the element is visible or not.
        :return: True if the element of visible, False otherwise.
        """

        if self._element is None:
            try:
                self._set_element()

            except NoSuchUIElement:
                return False

        return self._element.is_displayed()

    def is_enabled(self):
        """
        Checks if the element is enabled or not.
        :return: True if the element is enabled, False otherwise.
        """

        if self._element is None:
            try:
                self._set_element()

            except NoSuchUIElement:
                return False

        return self._element.is_enabled()

    def get_attribute(self, name):
        """
        Returns an attribute related to the element.
        :param name: the name of the attribute.
        :return: returns the value of the attribute.
        """

        if self._element is None:
            self._set_element()

        return self._element.get_attibute(name)

    def _is_interactable(self):
        """
        Checks if the element is interactable of not.
        * if it is enabled and visible.
        """

        if self._element is None:
            self._set_element()

        if self._element.is_displayed() and self._element.is_enabled():
            return True
        return False
