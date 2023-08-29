#!/usr/bin/python3
"""
1-square.py
class Square that defines a square by: (based on 0-square.py)
`Private instance attribute: size
Instantiation with size (no type/value verification)
"""


class Square:
    """ defines a square by: (based on 0-square.py)"""
    def __init__(self, size):
        self.__size = size
