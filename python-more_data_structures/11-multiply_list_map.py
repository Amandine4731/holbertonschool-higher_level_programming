#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    new_list = []
    for i in range(len(my_list)):
        if len(my_list) > 0:
            new_list.append(my_list[i] * number)
        else:
            return None
    return new_list
