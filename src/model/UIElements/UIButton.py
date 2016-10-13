"""
Module for degining a UIButton object.
"""
from src.StaticResources.StaticData import StaticData
from src.model.UIElements.UIObject import UIObject


class UIButton(UIObject):
    """
    UIButton object definitions.
    """
    def __init__(self, controller, element_tag):
        """
        Constructor.
        :param controller:
        :param element_tag:
        """
        super(UIButton, self).__init__(controller, element_tag)

    def click(self):
        """

        :return:
        """
        if self._element.is_displayed() and self._element.is_enabled():
            self._element.click()

    def text(self):
        """

        :return:
        """
        if self.__main_controller.CONFIG_COMMANDER.PLATFORM.type == StaticData.Config.ANDROID_PLATFORM_TAG:
            return self._element.text
        elif self.__main_controller.CONFIG_COMMANDER.PLATFORM.type == StaticData.Config.IOS_PLATFORM_TAG:
            return self.get_attribute("name")
