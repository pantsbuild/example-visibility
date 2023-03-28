import json


def read_json(filepath: str):
    with open(filepath) as fh:
        rectangles = json.load(fh)
    return rectangles
