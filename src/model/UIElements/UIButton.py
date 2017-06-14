"""
Module for degining a UIButton object.
"""
from src.model.UIElements.UIBaseElement import UIBaseElement


class UIButton(UIBaseElement):
    """
    UIButton object definitions.
    """
    def __init__(self, controller, element_tag=None, xpath=None):
        """
        Constructor.
        :param controller: a main controller for the application.
        :param element_tag: the tag associated with the button element.
        """

        super(UIButton, self).__init__(controller, element_tag, xpath)
        self.__initiated = True
