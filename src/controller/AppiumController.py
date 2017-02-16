"""
Module that handle the Appium logic.
"""
from src.StaticResources.StaticData import StaticData
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
        self.appium_driver = self.__appium_server_connection()

    def get_appium_instance(self):
        if self.__local_appium is not None:
            return self.__local_appium
        else:
            self.__local_appium = AppiumProxy.get_appium_instance()
            return self.__local_appium

    def get_element(self, elem_tag, xpath=None):
        if xpath is not None:
            return self.appium_driver.find_element_by_xpath(xpath)
        xpath = self.platform.get_element_xpath(elem_tag)
        try:
            if xpath is not None:
                return self.appium_driver.find_element_by_xpath(xpath)
            else:
                return self.appium_driver.find_element_by_name(elem_tag)
        except Exception as ex:
            raise ex

    def __appium_server_connection(self):
        appium_server_connection_data = self.platform.get_datails()
        return webdriver.Remote(StaticData.Config.Appium.SERVER_URL, appium_server_connection_data)
