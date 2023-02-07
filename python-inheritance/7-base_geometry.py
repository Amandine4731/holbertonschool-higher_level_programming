#!/usr/bin/python3
"""
Python program to return a list of object
"""


class BaseGeometry:
    """ class with public instance method """

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        elif int(value) <= 0:
            raise ValueError("{} must be greater than 0".format(name)) 
