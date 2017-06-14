"""
Module that handle the Appium logic.
"""
from settings import Settings
from src.model.Exceptions.UIExceptions import NoSuchUIElement
from src.model.appiumproxy import AppiumProxy
from appium import webdriver


class AppiumController(object):
    """
    Class that handles the Appium interaction logic.
    """

    __local_appium = None

    def __init__(self, platform):
        """
        Controller.
        """
        self.platform = platform
        self.appium_driver = None

    def get_appium_instance(self):
        """
        Returns an Appium server interface.
        """
        if self.__local_appium is not None:
            return self.__local_appium
        self.__local_appium = AppiumProxy.get_appium_instance()
        return self.__local_appium

    def get_element(self, elem_tag, xpath=None):
        """
        Returns a element from the app.
        :param elem_tag: an element tag associated with an xpath
        :param xpath: a direct xpath for the element.
        :return: returns an app Element
        """
        if xpath is not None:
            return self.appium_driver.find_element_by_xpath(xpath)
        _xpath = self.platform.get_element_xpath(elem_tag)
        try:
            if _xpath is not None:
                element_ = self.appium_driver.find_element_by_xpath(_xpath)
            else:
                element_ = self.appium_driver.find_element_by_name(elem_tag)
            return element_
        except Exception:
            raise NoSuchUIElement

    def connect(self):
        """
        Connects to the Appium server.
        """
        self.appium_driver = self.__appium_server_connection()

    def disconnect(self):
        """
        Disconnects from the Appium server.
        """
        self.appium_driver.close_app()
        self.appium_driver.close()

    def __appium_server_connection(self):
        """
        Uses the platform configuration in order to establish a new session to the service.
        :return: returns a driver for interaction with the service,
        """
        appium_server_connection_data = self.platform.get_details()
        return webdriver.Remote(Settings.Config.Appium.SERVER_URL, appium_server_connection_data)
