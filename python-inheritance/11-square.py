#!/usr/bin/python3
"""
Python program to return a list of object
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ class Square inherits from Rectangle """

    def __init__(self, size):
        self.__size = size

        self.__size == BaseGeometry.integer_validator(self, 'size', size)

    def area(self):
        """ return operation area """
        return self.__size ** 2

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__size, self.__size)
