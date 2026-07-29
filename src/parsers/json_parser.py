import json

def parse(path):

    with open(path) as f:
        return json.load(f)
