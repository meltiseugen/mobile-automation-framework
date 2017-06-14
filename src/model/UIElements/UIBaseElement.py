"""
UI element that acts as a container for other elements.
"""

from settings import Settings
from src.model.UIElements.UIObject import UIObject


class UIBaseElement(UIObject):
    """
    UI element that acts as a container for other elements.
    """

    def __init__(self, controller, element_tag=None, xpath=None):
        """
        Constructor.
        :param controller: a main controller for the application.
        :param element_tag: the tag associated with the button element.
        """
        super().__init__(controller, element_tag, xpath)
        self.__initiated = True

    def click(self):
        """
        Clicks the element.
        """

        if self._element is None:
            self._set_element()

        if self._element.is_displayed() and self._element.is_enabled():
            self._element.click()

    def text(self):
        """
        Returns the text.
        """

        if self._element is None:
            self._set_element()

        if self.__main_controller.CONFIG_COMMANDER.PLATFORM.type == Settings.Config.ANDROID_PLATFORM_TAG:
            return self._element.text

        elif self.__main_controller.CONFIG_COMMANDER.PLATFORM.type == Settings.Config.IOS_PLATFORM_TAG:
            return self.get_attribute("name")
