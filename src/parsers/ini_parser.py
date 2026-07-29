import configparser

def parse(path):

    parser = configparser.ConfigParser()
    parser.read(path)

    return parser
