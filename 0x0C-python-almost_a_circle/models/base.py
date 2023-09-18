#!/usr/bin/python3
# base.py

"""Defines class Base"""


class Base:
    """
    class base that has:
        private class attribute __nb_objects = 0
        class constructor: def __init__(self, id=None)
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
