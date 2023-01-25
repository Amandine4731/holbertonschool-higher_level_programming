#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    final_matrix = []
    for arr in matrix:
        for arr_in_arr in arr:
            new_matrix.append(arr_in_arr * arr_in_arr)
        final_matrix.append(new_matrix)
    return final_matrix
