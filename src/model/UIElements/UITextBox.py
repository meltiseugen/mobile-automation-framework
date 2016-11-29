"""
Module for defining a TextBox object.
"""
from src.StaticResources.StaticData import StaticData
from src.model.UIElements.UIObject import UIObject


class UITextBox(UIObject):
    """
    UITextBox definitions.
    """

    def __init__(self, controller, element_tag=None, xpath=None):
        """
        Constructor.
        :param controller:
        :param element_tag:
        """
        super(UITextBox, self).__init__(controller, element_tag, xpath)

    def click(self):
        """

        :return:
        """
        if self._element.is_displayed() and self._element.is_enabled():
            self._element.click()

    def set_text(self, value):
        # TODO clear the text field if it contains text.
        """

        :param value:
        :return:
        """
        self._element.send_keys(value)

    def text(self):
        """

        :return:
        """
        if self.__main_controller.CONFIG_COMMANDER.PLATFORM.type == StaticData.Config.ANDROID_PLATFORM_TAG:
            return self._element.text
        elif self.__main_controller.CONFIG_COMMANDER.PLATFORM.type == StaticData.Config.IOS_PLATFORM_TAG:
            return self.get_attribute("name")

    # TODO check if difference between text and value.
