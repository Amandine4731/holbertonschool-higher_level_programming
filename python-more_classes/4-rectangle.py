#!/usr/bin/python3
"""
Python program to create empty class that defines a rectangle
"""


class Rectangle:
    """ private class attribute """

    def __init__(self, width=0, height=0):
        """ private instance attribute """
        self.height = height
        self.width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

        if type(value) is not int:
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

        if type(value) is not int:
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

    def area(self):
        """ return operation area """
        return self.__height * self.__width

    def perimeter(self):
        """ return operation perimeter """
        if self.__height == 0 or self.__width == 0:
            return 0
        return (self.__height + self.__width) * 2

    def __str__(self):
        """ Instance method to return an informal printable string """
        if self.__height == 0 or self.__width == 0:
            return ""
        else:
            string = ""
            for i in range(self.__height):
                for j in range(self.__width):
                    string = string + "#"
                if i < self.__height - 1:
                    string = string + '\n'
            return string

    def __repr__(self):
        return f"Rectangle({self.__width}, {self.__height})"
