#!/usr/bin/python3
"""
Python program to return true or false
"""


def is_kind_of_class(obj, a_class):
    """ true if oject is an instance or a class that inherited from """
    if type(obj) is a_class:
        return True
    elif isinstance(obj, a_class):
        return True
    else:
        return False
