#!/usr/bin/python3
# 10-student.py

"""Defines a class Student"""


class Student:
    """class Student that has first_name, last_name and age"""
    def __init__(self, first_name="", last_name="", age=0):
        """instatiates class Student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__
        self_dict = {}
        for attr in attrs:
            if hasattr(self, attr):
                self_dict[attr] = getattr(self, attr)
        return (self_dict)
