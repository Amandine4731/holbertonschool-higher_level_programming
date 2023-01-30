#!/usr/bin/python3
"""
Python program to create empty class (square)
"""


class Square:
    """ private class attribute """
    __size = {}

    try:
        def __init__(self, size=0):
            """ private instance attribute """
            self.__size = size

            if size < 0:
                raise ValueError("size must be >= 0")

        def __display(self):
            """ print square """
            print(f"'Square' object has no attribute {self.__size}")
    except TypeError:
        print("size must be an integer")
