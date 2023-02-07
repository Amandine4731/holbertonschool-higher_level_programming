#!/usr/bin/python3
"""
Python program to return true if oject is an instance
"""


def inherits_from(obj, a_class):
    """ True if the object is an instance of a class that inherited from class """
    if type(obj) is a_class:
        return False
    elif isinstance(obj, a_class):
        return True
    else:
        return False
