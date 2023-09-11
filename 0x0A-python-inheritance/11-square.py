#!/usr/bin/python3
# 11-square.py

"""Define a Rectangle subclass Square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class Square that inherits from Rectangle"""

    def __init__(self, size):
        """Instatiates a new square
        Args:
            size (int): size of the square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
