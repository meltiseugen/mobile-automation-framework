"""
Module that holds the main controller.
"""
from src.controller.AppiumController import AppiumController
from src.controller.ConfigController import ConfigController
from src.controller.FileController import FileController


class MainController(object):
    """
    A class representing the main controller.
    """

    APPIUM = AppiumController()
    FILE_COMMANDER = FileController()
    CONFIG_COMMANDER = ConfigController()

    def __init__(self):
        """
        Constructor.
        """
        pass
