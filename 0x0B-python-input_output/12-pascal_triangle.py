#!/usr/bin/python3
# 12-pascal_triangle.py

"""Defines a function def pascal_triangle(n): that returns
a list of lists of integers representing the Pascal’s triangle of n
"""


def pascal_triangle(n):
    """Returns a list of integers representing pascal triangle n"""
    pascal_list = []
    if n <= 0:
        return pascal_list
    else:
        dec = 1
        for i in range(1, n + 1):
            row = []
            for j in range(1, i + 1):
                if i == j:
                    row.append(1)
                else:
                    row. append(i + j)
            pascal_list.append(row)
        return pascal_list
