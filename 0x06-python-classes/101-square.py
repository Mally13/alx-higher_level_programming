#!/usr/bin/python3
"""
101-square.py
class Square that defines a square by: (based on 6-square.py)
"""


class Square:
    """class Square that defines a square"""
    def __init__(self, size=0, position=(0, 0)):
        """set size the a square"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """get current positon of a square"""
        return (self.__position)

    @position.setter
    def position(self, value):
        """set the position of a square"""
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(coord, int) for coord in value) or
                not all(coord >= 0 for coord in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Public instance method: def area(self)
        returns the current square area
        """
        area = self.__size * self.__size
        return (area)

    def my_print(self):
        """prints a square"""
        if self.__size == 0:
            print("")
        else:
            for i in range(0, self.__position[1]):
                print("")
            for j in range(0, self.__size):
                print(" " * self.__position[0] + "#" * self.__size)

    def __str__(self):
        representation = ""
        if self.__size == 0:
            representation += "\n"
        else:
            for i in range(self.__position[1]):
                representation += "\n"
            for j in range(self.__size):
                representation += " " * self.__position[0] +
                "#" * self.__size + "\n"
        return representation.strip()
