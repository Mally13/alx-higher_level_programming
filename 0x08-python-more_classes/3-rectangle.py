#!/usr/bin/python3
# 3-rectangle.py


"""
class Rectangle that defines a rectangle by:
    Private instance attribute: width
    Private instance attribute: height
    Instantiation with optional width and height:
        def __init__(self, width=0, height=0)
    Public instance method: def area(self):
        that returns the rectangle area
    Public instance method: def perimeter(self):
        if width or height is equal to 0, perimeter is equal to 0
    print() and str() should print the rectangle:
        if width or height is equal to 0, return an empty string
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
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """calculates and returns area of the rectangle"""
        area = self.__width * self.__height
        return area

    def perimeter(self):
        """calculates the perimeter of a rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        perimeter = 2 * (self.__width + self.__height)
        return perimeter

    def __str__(self):
        """prints rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            my_rectangle = ""
            for i in range(self.__height):
                my_rectangle += ("#" * self.__width + '\n')
            return my_rectangle
