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
        self.__path_commander = PathCommander()
        self.__file_commander = FileCommander(self.__path_commander.get_resource())
        self.__folder_commander = FolderCommander()
        self.__appium = None

    @classmethod
    def start_appium(cls, main_commander):
        """
        Start appium
        :return: None
        """
        cls.__appium_starter = AppiumStarter(main_commander)
        cls.__appium_starter.start()

    @classmethod
    def stop_appium(cls):
        """
        Stop appium
        :return: None
        """
        if cls.__appium_starter is not None:
            cls.__appium_starter.stop()

    def get_path_commander(self):
        """
        Returns the path commander
        :return: PathCommander (Object)
        """
        return self.__path_commander

    def get_file_commander(self):
        """
        Returns file commander
        :return: FileCommander object
        """
        return self.__file_commander

    def get_folder_commander(self):
        """
        Returns folder commander
        :return: FolderCommander object
        """
        return self.__folder_commander

    def get_database_commander(self):
        """
        Return database connection
        :return: database connection
        """
        return self.__db_connection

    def connect_to_appium(self, platform_name):
        """
        Connect to appium and set the connection to the variable
        :param platform_name:
        :return:
        """
        data = self.get_file_commander().get_appium_connection_data(platform_name)
        self.__appium = AppiumConnection(data, platform_name)

    def get_appium_connection(self):
        """
        Returns appium connection
        :return: appium
        """
        if self.__appium is not None:
            return self.__appium
        else:
            raise AppiumError(message="No appium connection")
