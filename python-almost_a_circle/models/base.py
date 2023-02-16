#!/usr/bin/python3
"""
Python program
"""

import json


class Base:
    """ base class created """

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """ return json string """
        if list_dictionaries is not None:
            return json.dumps(list_dictionaries)
        else:
            return "[]"
