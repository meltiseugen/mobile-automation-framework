"""
Implementation of the test suite decorator.
"""

import inspect


def test_suite(test_suite_id: str):
    """
    Class decorator for UI flow classes
    Represents a suite
    Retrieves all methods that starts with "test" from the class and calls them in order
    Uses reflection
    :param test_suite_id: the name/id of the suite
    """
    def decorator(cls):
        """
        Decorator for the class
        :param cls: a pinter to the class
        """
        class Wrapper(object):
            """
            Wrapper over the class in order to change the behaviour.
            """
            def __init__(self):
                print("Launch Suite: " + test_suite_id)
                self.wrapped = cls()
                print("Retrieving test methods...")
                methods_ = inspect.getmembers(self.wrapped, predicate=inspect.ismethod)
                test_methods = list()
                for method in methods_:
                    if method[0].startswith("test"):
                        test_methods.append(method[0])
                print("Starting tests:")
                for test_method in test_methods:
                    getattr(self.wrapped, test_method)()

        return Wrapper
    return decorator
