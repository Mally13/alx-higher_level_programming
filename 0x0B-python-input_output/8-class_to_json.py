#!/usr/bin/python3
# 8-class_to_json.py

"""Defines a function that returns the dictionary description
with simple data structure (list, dictionary, string, integer and boolean)
for JSON serialization of an object"""


def class_to_json(obj):
    """returns dictionary description of an object"""
    obj_dict = {}
    for attr_name in dir(obj):
        if not attr_name.startswith("__"):
            attr_value = getattr(obj, attr_name)
            if isinstance(attr_value, (list, dict, str, int, bool)):
                obj_dict[attr_name] = attr_value
    return (obj_dict)
