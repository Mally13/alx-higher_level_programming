#!/usr/bin/python3
# 11-student.py

"""Defines class Student"""


class Student:
    def __init__(self, first_name, last_name, age):
        """Instantiates class Student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves dictionary respresentation of a Student instance"""
        self_dict = {}
        for attr_name in dir(self):
            if not attr_name.startswith("__"):
                attr_value = getattr(self, attr_name)
                if isinstance(attr_value, (list, dict, str, int, bool)):
                    self_dict[attr_name] = attr_value
        return (self_dict)

    def reload_from_json(self, json):
        """replaces all attributes of the Student instance"""
        if json["first_name"]:
            self.first_name = json["first_name"]
        if json["last_name"]:
            self.last_name = json["last_name"]
        if json["age"]:
            self.age = json["age"]
