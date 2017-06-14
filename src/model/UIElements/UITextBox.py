"""
Module for defining a TextBox object.
"""

from src.model.UIElements.UIBaseElement import UIBaseElement


class UITextBox(UIBaseElement):
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
        self.__initiated = True

    def set_text(self, value):
        """
        Types the given text in the text field.
        :param value: the value to be typed.
        """

        if self._element is None:
            self._set_element()

        if self.text() == value:
            return

        self._element.send_keys(value)
