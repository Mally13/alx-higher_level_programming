#!/usr/bin/python3
# 7-rectangle.py


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
    repr() should return a string representation of the rectangle to be
    able to recreate a new instance by using eval()
"""


class Rectangle:
    """Class Rectangle that defines a rectangle"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0, ):
        """Instantiate class Rectangle"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
        my_rectangle = ""
        if self.__width == 0 or self.__height == 0:
            return my_rectangle
        else:
            for i in range(self.__height):
                if i < (self.__height - 1):
                    my_rectangle += (str(
                        self.print_symbol) * self.__width + '\n')
                else:
                    my_rectangle += (str(self.print_symbol) * self.__width)
            return my_rectangle

    def __repr__(self):
        """Rectangle class representation"""
        return f'Rectangle({self.width}, {self.height})'

    def __del__(self):
        """Prints message on instance deletion"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
