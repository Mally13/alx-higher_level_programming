#!/usr/bin/python3
# 101-add_attribute.py

"""
Defines a function that adds a new attribute
to an object if it’s possible
"""
def add_attribute(obj, attr_name, attr_value):
    if hasattr(obj, '__dict__') or (
            hasattr(type(obj), '__slots__')
            and attr_name in type(obj).__slots__):
        setattr(obj, attr_name, attr_value)
    else:
        raise TypeError("can't add new attribute")
