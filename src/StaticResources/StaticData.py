"""
Module that contains static resources.
"""

class StaticData(object):
    """
    Main class for holding resources.
    """
    class Config(object):
        """
        Static values related to config information.
        """
        ANDROID_PLATFORM_TAG = "Android"
        IOS_PLATFORM_TAG = "iOS"

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
