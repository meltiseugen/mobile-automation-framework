"""
Module that holds program configuration data objects.
"""
from src.model.Platform import Platform


class ConfigController(object):
    """
    A class that holds program configuration data.
    """

    PLATFORM = Platform()

    def __init__(self):
        """
        Constructor.
        """
        pass