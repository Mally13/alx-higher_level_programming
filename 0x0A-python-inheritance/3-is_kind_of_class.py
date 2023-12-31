#!/usr/bin/python3
# 3-is_kind_of_class.py

"""
Define a function that returns True if the object is an instance
of, or if the object is an instance of a class that inherited from,
the specified class ; otherwise False.
"""


def is_kind_of_class(obj, a_class):
    """returns True if the object is an instance of a class"""
    return (isinstance(obj, a_class))
