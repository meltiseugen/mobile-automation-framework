class Console(object):

    def __init__(self):
        pass

    @staticmethod
    def print_line(*args, returns=False):
        if "{:s}" in args[0] or "{:d}":
            s = args[0].format(*args[1:])
            print(s)
        else:
            formatted_output = ""
            for arg in args:
                formatted_output += str(arg)
            if returns:
                return formatted_output
            else:
                print(formatted_output)

    @staticmethod
    def print(*args):
        formatted_output = ""
        for arg in args:
            formatted_output += str(arg)
        print(formatted_output, end="")