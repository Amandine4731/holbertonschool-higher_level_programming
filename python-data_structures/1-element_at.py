#!/usr/bin/python3
def element_at(my_list, idx):
    if idx == 0:
        return my_list[0]
    if idx < 0:
        return None
    if idx > 0 and idx <= len(my_list):
        return my_list.pop(idx)
