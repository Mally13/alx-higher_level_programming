#!/usr/bin/python3
# 2-is_same_class.py

"""
Define a function that returns True if the object is exactly
an instance of the specified class
"""


def is_same_class(obj, a_class):
    """Checks if if the object is exactly an instance of a class"""
    return (type(obj) is a_class)
