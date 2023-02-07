#!/usr/bin/python3
"""
Python program to return a list of object
"""


class BaseGeometry:
    """ class BaseGeometry """

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        elif int(value) <= 0:
            raise ValueError("{} must be greater than 0".format(name))

class Rectangle(BaseGeometry):
    """ class Rectangle inherits from BaseGeometry """

    def __init__(self, width, height):
        self.__width = width
        self.__height = height
