import subprocess
import time

from src.model.base_proxy import BaseProxy


class Charles(BaseProxy):

    URL_OF_SESSION_XML = "http://control.charles/session/export-xml"
    URL_OF_SESSION_HAR = "http://control.charles/session/export-har"
    URL_OF_SESSION_CSV = "http://control.charles/session/export-csv"

    SESSION_XML_FORMAT = "export-xml"
    SESSION_HAR_FORMAT = "export-har"
    SESSION_CSV_FORMAT = "export-csv"

    def __init__(self, path_to_bin, params):
        super(Charles, self).__init__(path_to_bin, None, params)

    def start(self):
        super(Charles, self).start()

    def record(self, time_to_wait=5):
        def record_process():
            shell_comm = "curl --silent -x localhost:8880 http://control.charles/recording/start > /dev/null"
            process = subprocess.Popen(shell_comm,
                                       shell=True,
                                       stdout=subprocess.PIPE,
                                       stderr=subprocess.PIPE)
            process.communicate()
        for _ in range(time_to_wait):
            record_process()
            time.sleep(1)

    def save_session(self, directory_path, file_name, format_type="export-xml"):
        shell_comm = "curl -x localhost:8880 http://control.charles/session/"+format_type+" -o "+directory_path+"/"+file_name+" "
        print(shell_comm)
        process = subprocess.Popen(shell_comm,
                                   shell=True,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE)
        process.communicate()
