#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return my_list
    else:
        a = my_list.copy()
        a.remove(idx + 1)
        a.insert(idx, element)
        return my_list and a
