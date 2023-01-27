#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        i = 0
        if x in my_list:
            while i < x:
                i += 1
                print(i, end='')
            print()
            return x
        else:
            while i < max(my_list):
                i += 1
                print(i, end='')
            print()
            return max(my_list)
    except:
        print("empty list")
