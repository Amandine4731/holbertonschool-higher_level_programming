#!/usr/bin/python3
"""
    Python program
"""


import json


def load_from_json_file(filename):
    """ create an Object from a "JSON file" """
    with open(filename, 'r') as f:
        stock = f.read()
    f.close()
    return (json.loads(stock))
