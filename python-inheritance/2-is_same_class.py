#!/usr/bin/python3
"""
Python program to return true if oject is an instance
"""


def is_same_class(obj, a_class):
    """ function to return true if oject is an instance """
    if type(obj) is a_class:
        return True
    else:
        return False
