#!/usr/bin/python3
# 0-add_integer.py
"""
Add two integers.
Args:
    a (int or float): The first number.
    b (int or float, optional): The second number. Default is 98.
Returns:
    int: The sum of a and b as an integer.
"""


def add_integer(a, b=98):
    """a function that adds 2 integers"""
    if not isinstance(a, (int,float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
