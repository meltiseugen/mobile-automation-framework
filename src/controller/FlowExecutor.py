class FlowExecutor(object):
    """

    """

    INPUT_KEYS = [
        "formatted_address",
        "geo_coordinates"
    ]

    EXPECTED_KEYS = [
        "address",
        "location"
    ]

    def __init__(self, flow_file):
        with open(flow_file) as fd:
            self.flow_file = xmltodict.parse(fd.read())
        fd.close()
        self.final_results = []

    def execute(self, execute_data):
        one_flow_results = []
        final_result = []

        def parse_dict(dictionary, input_, expected_):
            for key in dictionary:
                if key == "Rule":
                    result = ""
                    actual = None
                    exp = None
                    if dictionary[key]["@name"] == "check query":
                        pass
                    elif dictionary[key]["@name"] == "check coord":
                        pass
                    elif dictionary[key]["@name"] == "check address brand":
                       pass
                    try:
                        if result == "Passed":
                            parse_dict(dictionary[key][result], input_, expected_)
                        elif result == "Failed":
                            parse_dict(dictionary[key][result], input_, expected_)
                        elif result == "Na":
                            parse_dict(dictionary[key][result], input_, expected_)
                        elif result == "Warning":
                            parse_dict(dictionary[key][result], input_, expected_)
                    except KeyError:
                        raise Exception("Flow case: " + result + " for rule: " + str(dictionary[key]["@name"]) +
                                        " not addressed!")
                elif key == "@status":
                    if "@severity" in dictionary:
                        final_result.append(
                            (dictionary[key], dictionary["@severity"], one_flow_results, dictionary["@severity"]))
                    else:
                        final_result.append((dictionary[key], one_flow_results))
                else:
                    print(key)

        # input_ = filter_by_keys(execute_data[DataDictionary.INPUT], self.INPUT_KEYS)
        # expected_ = filter_by_keys(execute_data[DataDictionary.EXPECTED], self.EXPECTED_KEYS)
        # parse_dict(self.flow_file, input_, expected_)
        return final_result