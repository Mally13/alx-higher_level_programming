#!/usr/bin/python3
# 9-student.py

"""Defines a class Student"""


class Student:
    """class Student that has first_name, last_name and age"""
    def __init__(self, first_name="", last_name="", age=0):
        """instatiates class Student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        self_dict = {}
        for attr_name in dir(self):
            if not attr_name.startswith("__"):
                attr_value = getattr(self, attr_name)
                if isinstance(attr_value, (list, dict, str, int, bool)):
                    self_dict[attr_name] = attr_value
        return (self_dict)
