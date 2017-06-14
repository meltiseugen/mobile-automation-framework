"""
Module that contains static resources.
"""
import os


def _get_project_path():
    """
    Returns the path to the root of the project. Dynamically constructed.
    :return: returns str: the path to the project.
    """

    relative_path = os.getcwd()
    project_path_elements = relative_path.split("/")[1:]
    project_path = "/"
    for path_element in project_path_elements:
        if "requirements.txt" in os.listdir(project_path):
            return project_path
        else:
            project_path += path_element + "/"
    return project_path


class Paths(object):
    """
    Constants related to paths in the project.
    """
    PROJECT_PATH = _get_project_path()


class Settings(object):
    """
    Main class for holding static resources.
    """

    class Paths(object):
        """
        Constants related to paths in the project.
        """

        PROJECT_PATH = Paths.PROJECT_PATH
        RESOURCE_PATH = Paths.PROJECT_PATH + "resources/"
        OUTPUTS_PATH = Paths.PROJECT_PATH + "outputs/"
        SOURCE_PATH = Paths.PROJECT_PATH + "src/"
        DEVICE_DATA_PATH = RESOURCE_PATH + "device_data.json"
        UI_ELEMENTS_PATH = RESOURCE_PATH + "ui_elements.json"

    class Config(object):
        """
        Static values related to config information.
        """

        ANDROID_PLATFORM_TAG = "Android"
        IOS_PLATFORM_TAG = "iOS"

        class Appium(object):
            """
            Constants related to the Appium server.
            """
            PATH = "appium"
            PORT = "4444"
            SERVER_URL = "http://localhost:" + PORT + "/wd/hub"

    class Errors(object):
        """
        Static values related to errors
        """

        RETRY_NUMBER = 3

    class Waits(object):
        """
        Static values related to wait time.
        """

        SMALL_SLEEP_TIME = 1
        MEDIUM_SLEEP_TIME = 5
        LONG_SLEEP_TIME = 10

    class UIElements(object):
        """
        Static values of the UI elements for android and ios.
        """

        class Android(object):
            """
            Static values of the UI elements related to android.
            """

            DEFAULT_PATH = "devices.android.app_name.default_path"
