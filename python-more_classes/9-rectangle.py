#!/usr/bin/python3
"""
Python program to create empty class that defines a rectangle
"""


class Rectangle:
    """ private class attribute """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        Rectangle.number_of_instances += 1
        """ private instance attribute """
        self.height = height
        self.width = width
        Rectangle.print_symbol

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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if Rectangle.area(rect_1) == Rectangle.area(rect_2):
            return rect_1
        elif Rectangle.area(rect_1) > Rectangle.area(rect_2):
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        if size < 0:
            del(size)
        else:
            return cls(size, size)


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
                    string += str(self.print_symbol)
                if i < self.__height - 1:
                    string = string + '\n'
            return string

    def __repr__(self):
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        Rectangle.number_of_instances -= 1
        Rectangle.print_symbol
        print("Bye rectangle...")
        del(self.__width, self.__height)
        return
