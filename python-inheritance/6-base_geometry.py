#!/usr/bin/python3
"""
Python program to return a list of object 
"""


class BaseGeometry:
    """ class with public instance method """
    
    def area(self):
        raise Exception("area() is not implemented")
