#!/usr/bin/python3
# 2-matrix_divided.py

"""
Divides elements of matrix by div
Args:
    matrix: matrix to be divided
    div: an int or float to divide the matrix
Returns: a new matrix
"""


def matrix_divided(matrix, div):
    """Divides elements of a matrix"""
    if not all(isinstance(row, list) and all(isinstance(num, (int, float)) for num in row)
            for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if len(set(len(row) for row in matrix)) > 1:
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")
    
    divided_matrix = []
    for row in matrix:
        divided_row = [round(element / div, 2) for element in row]
        divided_matrix.append(divided_row)

    return divided_matrix
