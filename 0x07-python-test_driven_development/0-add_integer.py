#!/usr/bin/python3
# 0-add_integer.py
"""Add two integers:
a (int or float), b (int or float, optional Default is 98)
Returns:
    int: The sum of a and b as an integer.
"""


def add_integer(a, b=98):
    """a function that adds 2 ints and
    returns sum of a and b asan integer.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
