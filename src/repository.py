import json
import os

def load(path):

    if not os.path.exists(path):
        return {}

    with open(path, encoding="utf8") as f:
        return json.load(f)
