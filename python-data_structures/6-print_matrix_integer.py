#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for arr in matrix:
        i = 0
        for arr_in_arr in arr:
            i += 1
            if i == len(matrix):
                print("{:d}".format(arr_in_arr), end="")
            else:
                print("{:d}".format(arr_in_arr), end=" ")
        print()
