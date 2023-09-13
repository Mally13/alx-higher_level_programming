#!/usr/bin/python3
# 10-square.py

"""Define a Rectangle subclass Square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class Square that inherits from Rectangle"""

    def __init__(self, size):
        """Instatiates a new square
        Args:
            size (int): The size of the square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
