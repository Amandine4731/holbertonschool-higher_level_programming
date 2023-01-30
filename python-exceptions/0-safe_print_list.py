#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """
    THE REAL CODE
    try:
        i = 0
        while i != x:
            print(f"{my_list[i]}", end='')
            i += 1
        print()
        return i
    except:
        print()
        return i
    """
    try:
        i = 0
        if x in my_list:
            while i < x:
                i += 1
                print(i, end='')
            print()
            return x
        if x not in my_list and x > 0:
            while i < max(my_list):
                i += 1
                print(i, end='')
            print()
            return max(my_list)
        if x == 0:
            print()
            return 0
    except:
        print("empty list")
