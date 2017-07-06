"""
Proxy for the Charles web proxy.
"""
import subprocess
import time

from settings import Settings
from src.model.Exceptions.Charles import RecordNotStarted
from src.model.base_proxy import BaseProxy


class Charles(BaseProxy):
    """
    API class for the Charles web proxy.
    """

    URL_OF_SESSION_XML = "http://control.charles/session/export-xml"
    URL_OF_SESSION_HAR = "http://control.charles/session/export-har"
    URL_OF_SESSION_CSV = "http://control.charles/session/export-csv"

    SESSION_XML_FORMAT = "export-xml"
    SESSION_HAR_FORMAT = "export-har"
    SESSION_CSV_FORMAT = "export-csv"

    __CREATED = False

    def __init__(self, params, port):
        """
        Constructor.
        :param path_to_bin: Path to the charles executable.
        :param params: custom parameters.
        """
        if self.__CREATED is False:
            super(Charles, self).__init__("path_to_bin", None, params)
            self.__recording = False
            self.__port = port
            self.__running = False
        else:
            pass

    def start(self):
        """
        Start the charles server.
        """
        if not self.__running:
            super(Charles, self).start()
            time.sleep(Settings.Waits.MEDIUM_SLEEP_TIME)
        else:
            return

    def record(self):
        """
        Start recording (listening) for requests and responses.
        """

        def record_process():
            """
            Triggers the recording process on the charles server.
            """

            shell_comm = "curl --silent -x localhost:8880 http://control.charles/recording/start > /dev/null"

            process = subprocess.Popen(shell_comm, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            process.communicate()

        for _ in range(Settings.Waits.MEDIUM_SLEEP_TIME):
            record_process()
            time.sleep(Settings.Waits.SMALL_SLEEP_TIME)

        self.__recording = True

    def save_session(self, file_path, format_type="export-xml"):
        """
        Saves the current stored session from the charles service to the machine.
        :param file_path: the name of the file that will contain the session.
        :param format_type: the type of the format for the data.
                            Use class static fields for other options.
        """
        if self.__recording:
            session_location = None
            if format_type == Charles.SESSION_XML_FORMAT:
                session_location = Charles.URL_OF_SESSION_XML

            elif format_type == Charles.SESSION_CSV_FORMAT:
                session_location = Charles.URL_OF_SESSION_CSV

            elif format_type == Charles.URL_OF_SESSION_HAR:
                session_location = Charles.SESSION_HAR_FORMAT

            base_comm = "curl -x localhost:" + self.__port + " http://"
            shell_comm = base_comm + session_location + " -o " + file_path

            process = subprocess.Popen(shell_comm, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            process.communicate()

        else:
            raise RecordNotStarted()
