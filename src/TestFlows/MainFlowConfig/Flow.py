"""
Module that contains the basic Flow class configured to support running custom flows via INHERITANCE.
"""
import time

from settings import Settings
from src.controller.MainController import MainController


class Flow(object):
    """
    Base Flow class used to create a configuration environment for custom flows
    **** Intended as a super class
    """
    def __init__(self, platform):
        """
        Constructor.
        """
        self.platform = platform
        self.controller = MainController(platform)
        self.__start_appium()
        self.controller.appium.connect()
        time.sleep(Settings.Waits.MEDIUM_SLEEP_TIME)

    def __start_appium(self):
        """
        Starts the appium service
        Part of the setUp startup sequence.
        """

        self.controller.appium.get_appium_instance().start()

    def finalize(self):
        """
        Closes all links to the Appium service.
        Part of the tearDown finalize sequence.
        """
        self.controller.appium.disconnect()
        self.controller.appium.get_appium_instance().close()
