#!/usr/bin/python3
"""
4-square.py
class Square that defines a square by: (based on 3-square.py)
"""


class Square:
    """class Square that defines a square"""
    def __init__(self, size=0):
        """set size the a square"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        """get current size of the square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """set size the a square"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
            self.__size = value

    def area(self):
        """Public instance method: def area(self)
        returns the current square area
        """
        area = self.__size * self.__size
        return (area)
