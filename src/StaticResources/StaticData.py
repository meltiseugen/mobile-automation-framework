"""
Module that contains static resources.
"""
import os


def _get_project_path():
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

    """
    PROJECT_PATH = _get_project_path()


class StaticData(object):
    """
    Main class for holding resources.
    """

    class Paths(object):
        """

        """

        PROJECT_PATH = Paths.PROJECT_PATH
        RESOURCE_PATH = Paths.PROJECT_PATH + "resources/"
        OUTPUTS_PATH = Paths.PROJECT_PATH + "outputs/"
        SOURCE_PATH = Paths.PROJECT_PATH + "src/"

    class Config(object):
        """
        Static values related to config information.
        """
        ANDROID_PLATFORM_TAG = "Android"
        IOS_PLATFORM_TAG = "iOS"

        class Appium(object):
            PATH = "/Applications/Appium.app/Contents/Resources/node_modules/appium/build/lib/main.js"
            PORT = "4444"

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

    class UIElements(object):
        """
        Static values of the UI elements for android and ios.
        """
        class Android(object):
            """
            Static values of the UI elements related to android.
            """
            DEFAULT_PATH = "devices.android.app_name.default_path"

if __name__ == "__main__":
    print(StaticData.Paths.PROJECT_PATH)