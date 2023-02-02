#!/usr/bin/python3
"""
    function to divide all elements of a matrix
"""


def matrix_divided(matrix, div):
    """ function to divide all elements of a matrix """

    try:
        new_matrix = []
        final_matrix = []
        for arr in matrix:
            new_matrix = []
            for arr_in_arr in arr:
                if type(div) is int or type(div) is float:
                    new_matrix.append(round(float(arr_in_arr / div), 2))
                else:
                    raise TypeError("div must be a number")
                final_matrix.append(new_matrix)
            return final_matrix

    except TypeError:
        return "matrix must be a matrix (list of lists) of integers/floats"

    except ZeroDivisionError:
        if div == 0:
            return "division by zero"
