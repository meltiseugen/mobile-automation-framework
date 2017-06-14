"""
Module that holds the main controller.
"""
from settings import Settings
from src.controller.AppiumController import AppiumController
from src.controller.ResourceController import ResourceController


class MainController(object):
    """
    A class representing the main controller.
    """

    def __init__(self, platform):
        self.appium = AppiumController(platform)
        self.resource_controller = ResourceController(Settings.Paths.RESOURCE_PATH)
