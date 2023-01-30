#!/usr/bin/python3
"""
Python program to create empty class (square)
"""


class Square:
    """ private class attribute """
    def __init__(self, size=0):
        """ private instance attribute """
        self.__size = size

        if type(size) is not int:
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """ return operation square """
        return self.__size ** 2
