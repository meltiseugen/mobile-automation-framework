"""
Abstract class for input models.
"""

from abc import ABCMeta, abstractmethod


class Input(object):
    """
    Abstract class for input models.
    """

    __metaclass__ = ABCMeta

    @abstractmethod
    def from_stream(self, data):
        """
        Init the model with raw data given as a parameter.
        :param data: the raw data to be formatted with the model.
        """
        raise NotImplementedError

    @abstractmethod
    def from_file(self, file_path):
        """
        Init the model with raw data given from a file.
        :param file_path: teh path to the file.
        """
        raise NotImplementedError
