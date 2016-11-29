"""
File that contains a general class for building a dictionary.
"""
from collections import OrderedDict


class BaseDictionary(object):
    """
    Class that allows a simple set of operations for creating a dictionary like
    adding data to it and retrieving the data.
    """

    def __init__(self):
        """
        Constructor that initializes an empty dictionary.
        """
        self._dictionary = OrderedDict()
        self._parent = None

    def add(self, key, value):
        """
        Method that allows adding new data to the dictionary.
        :param key: The key for the data.
        :param value: The value for the key.
        :return: Returns a reference to the current instance of the class.
        """
        self._dictionary[key] = value
        return self

    def get_value(self, key):
        """
        Method that allows the retrieving of a value from a certain key.
        Throws a KeyError exception if the key is not present.
        :param key: The key for the value.
        :return: Returns the value associated to the given key.
        """
        try:
            return self._dictionary[key]
        except KeyError as ke:
            raise ke

    def keys(self):
        return self._dictionary.keys()

    def parse_dict(self, dic):
        """
        Method that formats a dictionary with all its inner dictionaries in a string format.
        """
        """
        Method that formats a dictionary with all its inner dictionaries in a string format.
        The result string will be a json format string.
        It handles the encoding of special unicode characters as well as the escaping of quotes.
        It supports as data types the followings:
        - BaseDictionaries: it converts the type into a json format
        - lists: it parses through the list and if the element is dict or BaseDictionary it will
        convert it to a json format, else it adds the string value to the json string.
        - dict: it converts the dict to a json format, much like it does when it coverts a
        BaseDictionary to a json format.
        - OrderedDict: which is a subclass of the dict class; behaves the same as with the dict
        :param dic: the main dictionary of type dict()
        :return: Returns a string with the contents of the main dictionary.
        """
        if isinstance(dic, str):
            return '"' + dic + '"'
        ds = "{"
        for key in dic.keys():
            if isinstance(dic[key], BaseDictionary):
                if ds == "{":
                    ds += '"' + str(key) + '": ' + str(self.parse_dict(dic[key].get_dictionary()))
                else:
                    ds += ', "' + str(key) + '": ' + str(self.parse_dict(dic[key].get_dictionary()))
            elif isinstance(dic[key], dict):
                if ds == "{":
                    ds += '"' + str(key) + '": ' + str(self.parse_dict(dic[key]))
                else:
                    ds += ', "' + str(key) + '": ' + str(self.parse_dict(dic[key]))
            elif isinstance(dic[key], list):
                if ds == "{":
                    s = "["
                    for e in range(0, len(dic[key]) - 1):
                        s += self.parse_dict(dic[key][e]) + ", "
                    s += self.parse_dict(dic[key][len(dic[key]) - 1])
                    s += "]"
                    ds += '"' + str(key) + '": ' + str(s)
                else:
                    s = "["
                    for e in range(0, len(dic[key]) - 1):
                        s += self.parse_dict(dic[key][e]) + ", "
                    s += self.parse_dict(dic[key][len(dic[key]) - 1])
                    s += "]"
                    ds += ', "' + str(key) + '": ' + str(s)
            elif isinstance(dic[key], str) or \
                    isinstance(dic[key], int) or \
                    isinstance(dic[key], bool) or \
                    isinstance(dic[key], float):
                if ds == "{":
                    formatted_string = str(str(dic[key]).encode("unicode_escape"))
                    if "b'" in formatted_string or 'b"' in formatted_string:
                        formatted_string = formatted_string.replace("b'", "").replace('b"', "")[0:-1]
                    formatted_string = formatted_string.replace('"', '\\"').replace("'", "\\'")
                    ds += '"' + str(key) + '": "' + formatted_string + '"'
                else:
                    formatted_string = str(str(dic[key]).encode("unicode_escape"))
                    if "b'" in formatted_string or 'b"' in formatted_string:
                        formatted_string = formatted_string.replace("b'", "").replace('b"', "")[0:-1]
                    formatted_string = formatted_string.replace('"', '\\"').replace("'", "\\'")
                    ds += ', "' + str(key) + '": "' + formatted_string + '"'
            else:
                raise Exception("The type " + str(type(dic[key])) + " is not supported")

        ds += "}"
        return ds

    def get_content(self):
        """
        Method that returns the dictionary content in a string format.
        :return: Returns the dictionary in a string format.
        """
        return self.parse_dict(self._dictionary)

    def get_dictionary(self):
        """
        Method that returns a reference to the inner dictionary.
        NOT quite recommended to use since it bypasses the class,
        but useful in some situations.
        :return: Returns a reference to the inner dictionary.
        """
        return self._dictionary

    def go_back_to(self, dic=None):
        """
        Method that returns the reference to the given dictionary.
        Used to maintain the flow of instructions.
        :param dic: The reference of the needed dictionary.
        :return: Returns the reference.
        """
        if dic is None:
            return self._parent
        else:
            return dic

    def add_dictionary(self, key):
        """
        Method that allows adding a dictionary to a key in the main dictionary.
        Usage example: dic.add("a", "A")
                          .add("b", "B")
                          .add_dictionary("Romania").add("CJ", "Cluj").add("HD", "Deva").GO_BACK_TO(dic)
                          .add("c", "C")
        :param key: The key for the inner dictionary.
        :return: Returns a reference to the inner dictionary.
        """
        inner_dict = BaseDictionary()
        self._dictionary[key] = inner_dict
        inner_dict._parent = self
        return inner_dict

    def pop_key(self, key, returns=True):
        """
        Method that removes a key from the dictionary.
        Remove specified key and return the corresponding
        value.
        If key is not found, returns is returned if given, otherwise KeyError
        is raised.
        :param key:
        :param returns:
        :return:
        """
        if returns:
            return self._dictionary.pop(key)
        else:
            self._dictionary.pop(key, None)

    def json_format(self):
        """
        Returns the dictionary in a json format.
        Much like the json.dumps method.
        :return: returns a string containing the dictionary in a json format.
        """
        return self.parse_dict(self._dictionary)

    def __getitem__(self, item):
        """
        Support for indexing: [item].
        :param item: the index or key.
        :return: the value of the index or key.
        """
        return self._dictionary[item]

    def __get__(self):
        """
        Class getter
        :return: return the inner dictionary.
        """
        return self._dictionary

    def __str__(self):
        """
        Descriptor for the str() method call.
        :return: Returns the dictionary in a string format.
        """
        return self.parse_dict(self._dictionary)

    def __repr__(self):
        """
        Does the same as __str__ but used when printing a list of BaseDictionary.
        Python str(list) calls in turn __repr__ on the objects inside.
        :return:
        """
        return self.parse_dict(self._dictionary)

    def __contains__(self, item):
        """

        :param item:
        :return:
        """
        return item in self._dictionary


if __name__ == "__main__":
    b = BaseDictionary()
    b.add("key", 'This is "my value: ß"')
    print(b)
