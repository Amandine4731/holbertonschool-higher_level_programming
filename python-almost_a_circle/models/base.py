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

    @staticmethod
    def to_json_string(list_dictionaries):
        """ return json string """
        if list_dictionaries is not None:
            return json.dumps(list_dictionaries)
        else:
            return "[]"

    @classmethod
    def save_to_file(cls, list_objs):
        """ to write json string of list_objs to a file """
        filename = "{}.json".format(cls.__name__)
        my_dict = []
        if list_objs is None and len(list_objs) <= 0:
            return "[]"
        else:
            for key in list_objs:
                my_dict.append(key.to_dictionary()) # in the file rectangle.py
        with open(filename, "w") as f:
            f.write(cls.to_json_string(my_dict))
