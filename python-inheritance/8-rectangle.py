#!/usr/bin/python3
"""
Python program to return a list of object
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ class Rectangle inherits from BaseGeometry """

    def __init__(self, width, height):
        self.__height = height
        self.__width = width

        self.__height == BaseGeometry.integer_validator(self, 'height', height)
        self.__width == BaseGeometry.integer_validator(self, 'width', width)
