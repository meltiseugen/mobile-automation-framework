"""
Module that contains the basic Flow class configured to support running custom flows via INHERITANCE.
"""
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

    def __start_appium(self):
        self.controller.APPIUM.get_appium_instance().start()

    def finalize(self):
        self.controller.APPIUM.get_appium_instance().close()
