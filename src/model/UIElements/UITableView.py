"""
Module for defining a UITableView object.
"""
from src.model.Exceptions.UIExceptions import TableChildIndexOutOfRange, NoSuchUIElement
from src.model.UIElements.UIObject import UIObject
from src.model.UIElements.UITableViewChildElement import UITableViewChildElement


class UITableView(UIObject):
    """
    UITableView definitions.
    """

    def __init__(self, controller, child_pattern, element_tag=None, xpath=None):
        """Constructor."""
        super(UITableView, self).__init__(controller, element_tag, xpath)
        self.__child_pattern = child_pattern
        self.__CHILDREN_COUNT = self.__count_children()

    def __generate_child_xpath(self, element_tag, child_pattern, child_index):
        """
        Generates a possible valid path of a child.
        :param element_tag: The xpath of the table view.
        :param child_pattern: The tag of the child.
        :param child_index: The number of the child.
        :return: returns a possible valid path to a child.
        """
        return element_tag + "/" + child_pattern + "[" + str(child_index) + "]"

    def __count_children(self):
        """

        :return:
        """
        done = False
        i = 1
        while not done:
            __may_be_child_path = self.__generate_child_xpath(self._element_tag, self.__child_pattern, i)
            try:
                self.__main_controller.APPIUM.get_element_by_xpath(__may_be_child_path)
            except NoSuchUIElement:
                done = True
            if done:
                break
            i += 1
        return i-1

    def get_child_by_index(self, child_index):
        """

        :param child_index:
        :return:
        """
        if child_index < 0 or child_index >= self.__CHILDREN_COUNT:
            raise TableChildIndexOutOfRange()
        __child_xpath = self.__generate_child_xpath(self._element_tag, self.__child_pattern, child_index)
        return UITableViewChildElement(self.__main_controller, xpath=__child_xpath)
