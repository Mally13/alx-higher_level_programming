#!/usr/bin/python3
"""
2-square.py
class Square that defines a square by: (based on 1-square.py)
with Private instance attribute: size
"""


class Square:
    """Defines a square"""
    def __init__(self, size=0):
        """
        Initialize a new Square with
        Private instance attribute: size
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
