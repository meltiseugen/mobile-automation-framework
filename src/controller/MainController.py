"""
Module that holds the main controller.
"""
from src.StaticResources.StaticData import StaticData
from src.controller.AppiumController import AppiumController
from src.controller.ResourceController import ResourceController


class MainController(object):
    """
    A class representing the main controller.
    """

    def __init__(self, platform):
        self.APPIUM = AppiumController(platform)
        self.RESOURCE_CONTROLLER = ResourceController(StaticData.Paths.RESOURCE_PATH)
