#!/usr/bin/python3
"""
Python program
"""


from models.base import Base


class Rectangle(Base):
    """ Class Rectangle inherits from Base """

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__id = id
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    """ width """
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, new_width):
        self.__width = new_width

    """ height """
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, new_height):
        self.__width = new_height

    """ x """
    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, new_x):
        self.__width = new_x

    """ y """
    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, new_y):
        self.__width = new_y
