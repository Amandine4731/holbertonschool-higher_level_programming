#!/usr/bin/python3
"""
    Python program
"""


def write_file(filename="", text=""):
    """ write a text file """
    with open(filename, 'w', encoding="utf-8") as f:
        f.write(text)

        return len(text)
