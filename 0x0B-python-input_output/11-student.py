#!/usr/bin/python3
# 11-student.py

"""Defines class Student"""


class Student:
    def __init__(self, first_name, last_name, age):
        """Instantiates class Student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves dictionary respresentation of a Student instance"""
        if attrs is None:
            return self.__dict__
        self_dict = {}
        for attr in attrs:
            if hasattr(self, attr):
                self_dict[attr] = getattr(self, attr)
        return (self_dict)

    def reload_from_json(self, json):
        """replaces all attributes of the Student instance"""
        if json:
            if json["first_name"] and self.first_name:
                self.first_name = json["first_name"]
            if json["last_name"] and self.last_name:
                self.last_name = json["last_name"]
            if json["age"] and self.age:
                self.age = json["age"]
