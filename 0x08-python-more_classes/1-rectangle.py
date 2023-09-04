#!/usr/bin/python3
# 1-rectangle.py


"""
class Rectangle that defines a rectangle by:
    Private instance attribute: width
    Private instance attribute: height
    Instantiation with optional width and height:
        def __init__(self, width=0, height=0)
"""


class Rectangle:
    """Class Rectangle that defines a rectangle"""

    def __init__(self, width=0, height=0):
        """Instantiate class Rectangle"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get reatangle width"""
        return self.__width

    @property
    def height(self):
        """Get rectangle height"""
        return self.__height

    @width.setter
    def width(self, value):
        """set rectangle width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """sets rectangle height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >=0")
        self.__height = value
