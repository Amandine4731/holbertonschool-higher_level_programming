#!/usr/bin/python3
def max_integer(my_list=[]):

        if len(my_list) == 0:
            return None

        if len(my_list) == 1:
            return my_list[0]

        else:
            my_list.sort()
            my_list.reverse()
            return my_list[0]
