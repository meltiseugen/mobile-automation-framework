"""
File used to establish the connection with the Appium server.
"""

import json
import os

import subprocess
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import WebDriverException, NoSuchElementException


class AppiumConnection(object):
    """
    The main class used to establish the connection with the Appium server
    and perform different kinds of operations
    """
    def __init__(self, url, connection_file, device_type):
        """
        Constructor for the AppiumConnection class.
        :param url: The URL on which the Appium server runs.
        :param connection_file: The jackson file containing the desired capabilities
                                required to configure the Appium server.
        :param device_type: The type of operating system that runs on the device
                            we wish to connect to; mainly iOS or Android
        """
        self.__url = url
        self.__connection_file = connection_file
        self.__device_type = device_type
        self.__driver = self.open_connection()

    def open_connection(self):
        """
        Method required for starting the connection with the Appium server.
        :return: returns a driver required for interacting and performing
                 different kinds on operations with the application.
        """
        with open(self.__connection_file) as json_data_file:
            data = json.load(json_data_file)
        for device in data:
            if device == self.__device_type:
                conn = data[device]
                conn["app"] = os.getcwd() + conn["app"]
                # conn["app"] = "/Users/eugenm/Desktop/app-debug.apk"
                json_data_file.close()
                return webdriver.Remote(self.__url, conn)

    def get_device_udid(self):
        """
        Method that returns the UDID of the connected Android device.
        :return: returns a string with the UDID of the device.
        """
        shell_comm = "adb devices"
        process = subprocess.Popen(shell_comm,
                                   shell=True,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE
                                   )
        result = process.communicate()[0]
        new_line_index = result.find("\n")
        result = result[new_line_index+1:]
        first_space = result.find("\t")
        result = result[:first_space]
        print "Found device with udid: " + str(result)
        return result

    def close_connection(self):
        """
        Method used to close the connection to the Appium server.
        """
        self.__driver.close_app()
        self.__driver.quit()

    def get_element(self, xpath):
        """
        Method used to return an element by its exclusive path.
        :param xpath: the complete exclusive path of the element.
        :return: returns the element corresponding to the exclusive path OR
                 raises a NoSuchElementException if the element can not be located
                 in the application.
        """
        try:
            return self.__driver.find_element_by_xpath(xpath)
        except NoSuchElementException as nsee:
            raise nsee

    def click_element(self, xpath):
        """
        Method that performs the click operation on an element given by its
        exclusive path.
        :param xpath: the exclusive path of the element that requires to be clicked.
        :return: N/A OR raises an exception if the element can not pe located
                 by its exclusive path
        """
        try:
            self.get_element(xpath).click()
        except Exception as nsee:
            print nsee

    def click(self, element):
        """
        Method that performs the click operation on an element.
        :param element: the element that requires to be clicked.
        """
        element.click()

    def get_touch_action(self):
        """
        Method that returns a TouchAction object.
        :return: returns a TouchAction instance.
        """
        return TouchAction(self.__driver)

    def get_current_activity(self):
        """
        Method that returns the current activity of the application
        :return: returns the current activity of the application
        """
        return self.__driver.current_activity

    def hide_keyboard(self):
        """
        Method that closes the OPENED keyboard on the application
        :return: N/A or raises a WebDriverException in case the keyboard is
                 NOT present on the application
        """
        try:
            self.__driver.hide_keyboard()
        except WebDriverException:
            pass

    def tap(self, positions):
        """
        Method that performs the tap operation at the given coordinates.
        Can perform multi-touch.
        :param positions: a LIST of TUPLES with two elements x and y containing
                          the desired coordinates.
        """
        self.__driver.tap(positions)

    def get_network_connection(self):
        """
        Method that returns the current network status of the device.
        :return: returns the network state of the device:
                    - NO INTERNET CONNECTION = 0
                    - WIFI INTERNET CONNECTION = 2
                    - DATA INTERNET CONNECTION = 4
                    - ALL INTERNET CONNECTION = 6
        """
        return self.__driver.network_connection

    def turn_location_on(self):
        """
        Method that toggles location services on.
        """
        self.__driver.toggle_location_services()
