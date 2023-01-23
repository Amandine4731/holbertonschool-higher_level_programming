#!/usr/bin/python3
def no_c(my_string):
    for i in range(0, len(my_string)):
        if my_string[i] == 'c' and my_string[i] == 'C':
            index = my_string.index(my_string[i])
            my_string = my_string.remove(index)
        return my_string
