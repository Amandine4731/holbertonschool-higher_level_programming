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
        if not list_objs or list_objs is None:
            my_dict = []
        else:
            for key in list_objs:
                my_dict.append(key.to_dictionary())  # in the file rectangle.py
        with open(filename, "w") as f:
            f.write(cls.to_json_string(my_dict))

    def from_json_string(json_string):
        """ to return the list of json """
        jsonstr = json.dumps(json_string)
        return jsonstr
