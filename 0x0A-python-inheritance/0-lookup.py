#!/usr/bin/python3
# 0-lookup.py

"""Define a function that returns the list of available attributes
and methods of an object
"""


def lookup(obj):
    """returns the list of available attributes and methods"""
    return dir(obj)
