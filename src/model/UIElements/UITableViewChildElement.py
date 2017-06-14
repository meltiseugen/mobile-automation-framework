"""
Module for defining a UITableViewChildElement object.
"""
from src.model.UIElements.UIBaseElement import UIBaseElement


class UITableViewChildElement(UIBaseElement):
    """
    UIButton object definitions.
    """

    def __init__(self, controller, element_tag=None, xpath=None):
        """
        Constructor.
        :param controller: a reference to the main controller.
        :param element_tag: the tag of the element.
        :param xpath: teh direct xpath for the element.
        """

        super(UITableViewChildElement, self).__init__(controller, element_tag, xpath)
        self.__initiated = True
