#!/usr/bin/python3
# 4-inherits_from.py

"""
 a function that returns True if the object is an instance
 of a class that inherited (directly or indirectly) from the specified
 class ; otherwise False.
"""


def inherits_from(obj, a_class):
    """checks if an object is a subclass"""
    return (isinstance(obj, a_class) and type(obj) is not a_class)
