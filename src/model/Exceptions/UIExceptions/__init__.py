"""
UIException definitions.
"""


class UIMainException(Exception):
    """
    Main Exception class for UiObjects.
    """
    _BASE_MESSAGE = ""

    def __init__(self, message=None):
        """
        Constructor.
        :param message:
        """
        if message is None:
            super(UIMainException, self).__init__(self._BASE_MESSAGE)
        else:
            super(UIMainException, self).__init__(message)


class NoSuchUIElement(UIMainException):
    """
    Exception for not finding an element.
    """
    _BASE_MESSAGE = "Element not found."

    def __init__(self, message=None):
        """
        Constructor.
        :param message:
        """
        if message is None:
            super(NoSuchUIElement, self).__init__(self._BASE_MESSAGE)
        else:
            super(NoSuchUIElement, self).__init__(message)


class TableChildIndexOutOfRange(UIMainException):
    """
    Exception for not finding a child in a table view by index.
    In case the index is not between the reachable bounds.
    """
    _BASE_MESSAGE = "Child index out of range."

    def __init__(self, message=None):
        """
        Constructor.
        :param message:
        """
        if message is None:
            super(TableChildIndexOutOfRange, self).__init__(self._BASE_MESSAGE)
        else:
            super(TableChildIndexOutOfRange, self).__init__(message)
