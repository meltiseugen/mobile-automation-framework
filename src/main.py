"""
A file that holds the main flow of the project.
"""

import sys
import unittest

from src.testComponents.test_android import TestAndroid

if __name__ == '__main__':
    """
    The test suite is formed and unittest classes are added.
    """
    print "starting main"
    if len(sys.argv) >= 2:
        print sys.argv
        try:
            print sys.argv
            if sys.argv[1] == "Android":
                suite = unittest.TestSuite()
                """add more test classes here"""
                suite.addTest(unittest.makeSuite(TestAndroid))
                unittest.TextTestRunner(verbosity=2).run(suite)
            elif sys.argv[1] == "iOS":
                suite = unittest.TestSuite()
                """add more test classes here"""
                unittest.TextTestRunner(verbosity=2).run(suite)
        except Exception as e:
            print e
    else:
        try:
            suite = unittest.TestSuite()
            """add more test classes here"""
            suite.addTest(unittest.makeSuite(TestAndroid))
            unittest.TextTestRunner(verbosity=2).run(suite)
        except Exception as e:
            print e

