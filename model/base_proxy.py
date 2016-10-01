"""
A file that contains a basic class for interacting with processes.
"""

import subprocess


class BaseProxy(object):
    """
    A basic class that contains the methods required to start and stop a process.
    """

    def __init__(self, path_to_bin, output_file=None, params=None):
        """
        Constructor for the class.
        :param path_to_bin: the name of the main program to run given directly by
                            its name if it present in the PATH or
                            given by its exclusive path.
        :param output_file: the name of the file used to store the output of the
                            process during every run.
        :param params: the required params needed to specify a certain behaviour
                       for the program.
        """
        self.__path_to_bin = path_to_bin
        self.__process = None
        self.__params = params
        self.__output_file = output_file

    def start(self):
        """
        Method that starts the process using the arguments presented in the constructor.
        The output of the process is redirected to a file also given in the constructor;
        the file is overwritten on every run.
        The process is locally stored for later use and especially to be later used to
        kill the process.
        :return: returns the process for external use
        """
        shell_comm = self.__path_to_bin
        for param in self.__params:
            shell_comm = shell_comm + " " + param
        print shell_comm
        if self.__output_file is not None:
            print "output file specified"
            with open(self.__output_file, 'w') as out_file:
                self.__process = subprocess.Popen(shell_comm,
                                                  shell=True,
                                                  stdout=out_file,
                                                  stderr=out_file
                                                  )
        else:
            print "output file NOT specified"
            self.__process = subprocess.Popen(shell_comm,
                                              shell=True,
                                              stdout=subprocess.PIPE,
                                              stderr=subprocess.PIPE
                                              )
        return self.__process

    def close(self):
        """
        Method used to kill the process that was started beforehand.
        """
        if self.__process is not None:
            self.__process.kill()
