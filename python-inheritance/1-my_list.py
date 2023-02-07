#!/usr/bin/python3
"""
Python program to create a list that inherits from an other list
"""


class MyList(list):
    """ private class attribute """

    def print_sorted(self):
        """ print the list sorted """
        print(sorted(self))
