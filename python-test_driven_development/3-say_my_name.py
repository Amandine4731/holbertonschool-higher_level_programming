#!/usr/bin/python3
"""
    function to print name
"""


def say_my_name(first_name, last_name=""):
    """ function to print name """

    try:
        if type(first_name) is str and type(last_name) is str:
            print("My name is {} {}".format(first_name, last_name))

    except TypeError:
        if type(first_name) is not str:
            return "first_name must be a string"
        elif type(last_name) is not str:
            return "last_name must be a string"
