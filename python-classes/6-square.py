#!/usr/bin/python3
"""
Python program to create empty class (square)
"""


class Square:
    """ private class attribute """
    def __init__(self, size=0, position=(0, 0)):
        """ private instance attribute """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """ property to retrieve it (size) """
        return self.__size

    @size.setter
    def size(self, value):
        """ property to set it (size) """
        self.__size = value

        if type(value) is not int:
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

    @property
    def position(self):
        """ property to retrieve it (position) """
        return self.__position

    @position.setter
    def position(self, value):
        """ property to set it (position) """
        self.__position = value
        
        if len(value) == 0:
            value = (0, 0)
        elif len(value) == 1:
            value = (value[0], 0)
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(value) == 2:
            value = (value[0], value[1])

            if value[1] < 0:
                raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """ return operation square """
        return self.__size ** 2

    def my_print(self):
        """ to print in stdout the square with the character # """
        if self.__size == 0:
            print()
        for pos1 in range(self.__position[1]):
            print()
        for i in range(self.__size):
            for pos2 in range(self.__position[0]):
                print(end=" ")
            for j in range(self.__size):
                print("#", end='')
            print()
