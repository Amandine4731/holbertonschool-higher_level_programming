#!/usr/bin/python3
"""
Python program to create empty class (square)
"""


class Square:
    """ private class attribute """
    def __init__(self, size=0):
        """ private instance attribute """
        self.__size = size

    @property
    def size(self):
        """ property to retrieve it """
        return self.__size

    @size.setter
    def size(self, value):
        """ property to set it """
        self.__size = value

        if type(value) is not int:
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """ return operation square """
        return self.__size ** 2

    def my_print(self):
        """ to print in stdout the square with the character # """
        if self.__size == 0:
            print()
        for i in range(self.__size):
            for j in range(self.__size):
                print('#', end='')
            print()
