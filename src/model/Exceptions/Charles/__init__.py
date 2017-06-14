"""
Custom exceptions used for the Charles web proxy proxy and API.
"""


class RecordNotStarted(Exception):
    """
    Main Exception class for UiObjects.
    """
    _BASE_MESSAGE = "Record not started on the service. Please use the record() method beforehand."

    def __init__(self, message=None):
        """
        Constructor.
        :param message: a custom message, overwriting the basic one.
        """
        if message is None:
            super(RecordNotStarted, self).__init__(self._BASE_MESSAGE)
        else:
            super(RecordNotStarted, self).__init__(message)
