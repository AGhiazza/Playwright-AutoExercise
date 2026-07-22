import json
import os

def read_json(filename):
    base = os.path.dirname(os.path.dirname(__file__))
    path = os.path.join(base, "data", filename)
    with open (path, encoding="utf-8") as file:
        return json.load(file)
