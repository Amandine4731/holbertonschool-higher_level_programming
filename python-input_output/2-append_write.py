#!/usr/bin/python3
"""
    Python program
"""


def append_write(filename="", text=""):
    """ read a text file """
    with open(filename, 'a+', encoding="utf-8") as f:
        f.read()
        f.write(text)

        f.close()
        return len(text)
