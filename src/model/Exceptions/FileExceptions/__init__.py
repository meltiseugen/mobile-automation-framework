

class FileMainException(Exception):
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
            super(FileMainException, self).__init__(self._BASE_MESSAGE)
        else:
            super(FileMainException, self).__init__(message)


class NotFound(FileMainException):
    """
    Exception for not finding an element.
    """
    _BASE_MESSAGE = "File not found."

    def __init__(self, message=None):
        """
        Constructor.
        :param message:
        """
        if message is None:
            super(NotFound, self).__init__(self._BASE_MESSAGE)
        else:
            super(NotFound, self).__init__(message)