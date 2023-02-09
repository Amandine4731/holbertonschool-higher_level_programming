#!/usr/bin/python3
"""
    Python program
"""


import json


def save_to_json_file(my_obj, filename):
    """ return an object represented by a JSON string """
    with open(filename, 'w') as f:
        return json.dumps(my_obj)
