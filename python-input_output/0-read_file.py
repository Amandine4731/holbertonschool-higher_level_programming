#!/usr/bin/python3
"""
    Python program
"""


def read_file(filename=""):
    """ read a text file """
    with open(filename, encoding="utf-8") as f:
        print(f.read())
