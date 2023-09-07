#!/usr/bin/python3
# 4-print_square.py

"""
print_square: prints a square

Args:
    size: size of the side of the square
"""


def print_square(size=None):    
    """prints a square"""
    if size == None:
        raise ValueError("enter size")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size-1):
            print("#", end="")
        print("#")
