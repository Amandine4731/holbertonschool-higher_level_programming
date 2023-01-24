#!/usr/bin/python3
def max_integer(my_list=[]):
    for i in my_list:
        if i > 1:
            my_list.sort()
            my_list.reverse()
        if i == 0:
            return None
    return my_list[0]
