"""
Implementation of the test case decorator.
"""

import json

import sys
import traceback


def test_case(name):
    """
    real decorator for test case functions.
    :param name: the name/code/id of the test case
    :return:
    """
    def decorator(function):
        """
        Inner decorator that accepts parameters
        :param+ function: the function on which the decorator will be applied
        :return:
        """
        def wrapper(*args, **kwargs):
            """
            Wrapper for the function
            :param args: arguments and keyword arguments for the function
            :param kwargs:
            :return:
            """
            with open("resources/test_data.json") as test_data_file:
                try:
                    test_data = json.load(test_data_file)[name]
                    kwargs["test_data"] = test_data
                    print("*** Test Case: " + name + " ***")
                    function(*args, **kwargs)
                    print("Done\n")
                except KeyError:
                    print("****** Error ******", file=sys.stderr)
                    traceback.print_stack()
                    print("Test data for " + name + " not found!", file=sys.stderr)
                except Exception as ex:
                    print("****** Error ******\n\t"+str(ex), file=sys.stderr)
                    traceback.print_stack()
        return wrapper
    return decorator
