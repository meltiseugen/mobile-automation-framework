"""
Module that handles interactions with various types of files.
"""


class FileController(object):
    """
    A class that allows interaction with different file types.
    """
    def __init__(self, base_path):
        """
        Initialization
        :param base_path: contains the path to the resources folder
        """
        self.__base_path = base_path

    @staticmethod
    def exists(file_path):
        """
        Returns it the requested file exists or not
        :param file_path: path to file
        :return: boolena
        """
        if os.path.isfile(file_path):
            return True
        raise NotFound(message="File Not Found!", error=None)

    @staticmethod
    def get_data(file_path, tags):
        """
        Returns the requested data
        :param file_path: location to the file
        :param tags: the tag path in the file (XML/JSON)
        :return: precious data (String)
        """
        if FileCommander.exists(file_path=file_path):
            if ".json" in file_path:
                data_reader = JSONOperator(file_path)
                return data_reader.get(tags)
            if ".xml" in file_path:
                data_reader = XMLOperator(file_path)
                return data_reader.get(tags)
        raise NotFound(message="File not XML or JSON!\nPATH: " + file_path, error=None)

    @staticmethod
    def get_files_in_dir(path):
        ret_files = []
        for root, dirs, files in os.walk(path):
            for file in files:
                if ".json" in file or ".xml" in file:
                    ret_files.append(os.path.join(root, file))
        return ret_files

    @staticmethod
    def get_search_input_data(arguments):
        """
        :param arguments: dict(path, group, locale, type)
        :return: List of input data
        """
        output_data = []
        file_dir_list = FolderCommander.get_input_data_folders(arguments)
        for files in file_dir_list:
            for f in FileCommander.get_files_in_dir(files):
                output_data.append(FileCommander.get_data(f, StaticDATA.DataTag.XML_INPUT_TAG))
            return output_data

    def get_appium_connection_data(self, device_name):
        """
        Returns data for appium connection
        :return:
        """
        data = FileCommander.get_data(file_path=self.__base_path + "/" + StaticDATA.Config.MAIN_CONFIG_FILE,
                                      tags=None)
        output_data = dict()
        output_data[StaticDATA.Config.URL] = data[StaticDATA.Config.APPIUM_CONFIG_TAG][StaticDATA.Config.URL]
        output_data[StaticDATA.Config.DEVICE] = data[StaticDATA.Config.DEVICE][device_name]
        return output_data

    def get_appium_start_configurations(self):
        """
        Returns appium default startup ata
        :return:
        """
        data = FileCommander.get_data(file_path=self.__base_path + "/" + StaticDATA.Config.MAIN_CONFIG_FILE,
                                      tags=StaticDATA.Config.APPIUM_CONFIG_TAG)

        output_data = dict(node_parameters=[str(data[StaticDATA.Config.NODE_JS_PATH]),
                                            str(data[StaticDATA.Config.APPIUM_PORT]),
                                            str(data[StaticDATA.Config.DEBUG_LOG])],
                           node_executable=str(data[StaticDATA.Config.NODE_EXEC]))
        return output_data

    @staticmethod
    def get_next_log_file(main_commander):
        path = main_commander.get_path_commander().get_output_location()
        main_commander.get_folder_commander().create_if_not_exists(path=path)
        return path + "/appium_" + time.strftime("%Y_%m_%d_%H_%M") + ".log"
