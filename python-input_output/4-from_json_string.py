#!/usr/bin/python3
"""
    Python program
"""


import json


def from_json_string(my_str):
    """ return an object represented by a JSON string """
    return json.loads(my_str)
