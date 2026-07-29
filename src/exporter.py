import json

def export(data):

    with open(
        "data/exports/config.json",
        "w"
    ) as f:

        json.dump(data, f, indent=4)
