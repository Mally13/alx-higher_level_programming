#!/usr/bin/python3
"""
3-square.py
class Square that defines a square by: (based on 2-square.py)
Private instance attribute: size
Instantiation with optional size: def __init__(self, size=0)
Public instance method: def area(self): that returns the current square area
"""


class Square:
    """class Square that defines a square by: (based on 2-square.py)"""
    def __init__(self, size=0):
        """Private instance attribute: size"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Public instance method: def area(self)
        that returns the current square area
        """
        area = self.__size * self.__size
        return (area)
