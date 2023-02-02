#!/usr/bin/python3
"""
    function to print square
"""


def print_square(size):
    """ function to print square """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    else:
        if int(size) < 0:
            raise ValueError("size must be >= 0")
        else:
            for i in range(size):
                for j in range(size):
                    if j != (size - 1):
                        print('#', end='')
                    else:
                        print("#")
                print()
