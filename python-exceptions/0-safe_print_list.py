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
        elif x not in my_list and x > 0:
            while i < max(my_list):
                i += 1
                print(i, end='')
            print()
            return max(my_list)
        else:
            return 0
    except:
        print("empty list")
