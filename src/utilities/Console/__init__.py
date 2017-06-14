"""
Logger implementation.
"""
import sys


class Console(object):
    """
    Logger implementation.
    Can be enabled or disabled.
    """

    def __init__(self, enabled=True):
        """
        Constructor.
        :param enabled: enables or disables the prints.
        """

        self._is_enabled = enabled

    def print_line(self, *args):
        """
        Prints the text in the standard output.
        :param args: the list of values to print.
        """

        if not self._is_enabled:
            return

        if "{:s}" in args[0] or "{:d}":
            formatted_string = args[0].format(*args[1:])
            print(formatted_string)

        else:
            formatted_output = ""
            for arg in args:
                formatted_output += str(arg)

            print(formatted_output)

    def print(self, *args):
        """
        Prints one line of text, without a new line at the end
        :param args: the list of values to print.
        """

        if not self._is_enabled:
            return

        formatted_output = ""
        for arg in args:
            formatted_output += str(arg)

        print(formatted_output, end="")

    def warning(self, *args):
        """
        Prints a line of text in the standard error file.
        :param args:  the list of values to print.
        """

        if not self._is_enabled:
            return

        formatted_output = ""
        for arg in args:
            formatted_output += str(arg)

        print(formatted_output, file=sys.stderr)
