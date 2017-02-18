from abc import ABCMeta, abstractmethod


class Input():
    __metaclass__ = ABCMeta

    @abstractmethod
    def from_stream(self, data):
        raise NotImplementedError

    @abstractmethod
    def from_file(self, data):
        raise NotImplementedError
