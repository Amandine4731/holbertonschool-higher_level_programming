#!/usr/bin/python3
"""
Python program
"""


from models.base import Base


class Rectangle(Base):
    """ Class Rectangle inherits from Base """

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    """ width """
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, new_width):
        self.__width = new_width
        if type(new_width) is not int:
            raise TypeError("width must be an integer")

        if new_width <= 0:
            raise ValueError("width must be > 0")

    """ height """
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, new_height):
        self.__height = new_height

        if type(new_height) is not int:
            raise TypeError("height must be an integer")

        if new_height <= 0:
            raise ValueError("height must be > 0")

    def area(self):
        """ function area """
        return self.__width * self.height

    def display(self):
        """ print the rectangle "#" """
        if self.__width == 0 or self.__height == 0:
            print()
        for pos in range(self.__y):
            print(end="\n" if self.__y > 0 else "")
        for i in range(self.__height):
            for pos in range(self.__x):
                print(end=" ")
            for j in range(self.__width):
                print('#', end='')
            print()

    """ x """
    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, new_x):
        self.__x = new_x

        if type(new_x) is not int:
            raise TypeError("x must be an integer")

        if new_x < 0:
            raise ValueError("x must be >= 0")

    """ y """
    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, new_y):
        self.__y = new_y

        if type(new_y) is not int:
            raise TypeError("y must be an integer")

        if new_y < 0:
            raise ValueError("y must be >= 0")

    def __str__(self):
        """ return a sentence """
        return ("[Rectangle] ({}) {}/{} - {}/{}".format
                (self.id, self.x, self.y, self.width, self.height))

    def update(self, *args):
        self.id = args[0]
        for i in range(len(args)):
            if i >= 1:
                self.width = args[1]
            if i >= 2:
                self.height = args[2]
            if i >= 3:
                self.x = args[3]
            if i > 3:
                self.y = args[4]
            else:
                self.id = args[0]
