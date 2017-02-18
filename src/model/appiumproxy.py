"""
An API used to directly start and interact with an Appium Process from Python.
The main class that provides this functionality is the Appium class.
"""
import os
import subprocess
import time

from src.StaticResources.StaticData import StaticData
from src.model.base_proxy import BaseProxy


class AppiumProxy(BaseProxy, object):
    """The proxy used for starting and controlling an Appium process.
    It inherits the two methods, start and stop, from the base class BaseProxy.
    The method 'start_appium' is used the start the server and the method 'close'
    is used to stop the process.
    """

    def __init__(self, bin, params, output_file):
        """
        Constructor for instantiating the class Appium. That in its turn calls the
        constructor of the base class.
        PRE-CONDITIONS: - params = a list of string arguments containing setup parameters
                                   required for starting Appium.
                                 = the first parameter must be the location of the main.js
                                   file of Appium.
                        - output_file = The name of the file (usually text file) where
                                        the Appium log will be printed and saved until
                                        the next run.
        POST-CONDITIONS: N/A.
        """
        self.__output = output_file
        self.__port = params[params.index("--port")+1]
        super(AppiumProxy, self).__init__(bin, output_file, params)

    def start(self, initial_wait_time=5):
        """
        Method used to start the Appium process using the parameters defined in
        the constructor.
        In its turn it calls the start method from the base class that initiates a
        subprocess with the Appium server running on it.
        It reserves a time frame of 5 seconds in which it allows the server to fully
        start and afterwards prints a message announcing the user that the server is
        ready for use.
        PRE-CONDITIONS: N/A.
        POST-CONDITIONS: N/A.
        """
        self.kill_process()
        super(AppiumProxy, self).start()
        time.sleep(initial_wait_time)

    def kill_process(self):
        shell_comm = "kill -kill `lsof -t -i tcp:" + self.__port + "`"
        process = subprocess.Popen(shell_comm, shell=True)
        process.communicate()
        print("killed process")
        time.sleep(5)

    @staticmethod
    def get_appium_instance():
        return AppiumProxy("node",
                      [StaticData.Config.Appium.PATH,
                       "--port", StaticData.Config.Appium.PORT,
                       "--debug-log-spacing"
                       ],
                      StaticData.Paths.OUTPUTS_PATH + "appium-out-file.txt"
                      )
