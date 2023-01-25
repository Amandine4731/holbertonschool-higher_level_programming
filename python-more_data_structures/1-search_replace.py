#!/usr/bin/python3
def search_replace(my_list, search, replace):
    for i in range(len(my_list)):
        if my_list != 0:
            if my_list[i] == search:
                if replace == 0:
                    my_list[i] = 0
                else:
                    my_list[i] = replace
        else:
            return None
    return my_list
