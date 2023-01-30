#!/usr/bin/python3
"""
Python program to create empty class (square)
"""


class Square:
    """ private class attribute """
    __size = {}

    def __init__(self, __size):
        """ private instance attribute """
        self.__size = __size

    def __display(self):
        """ print square """
        print(f"'Square' object has no attribute {self.__size}")
