#!/usr/bin/python3
# 3-say_my_name.py

"""
function say_my_name: Prints my name
Args:
    first_name: My first name
    last_mame: My last name
"""


def say_my_name(first_name="", last_name=""):
    """Prints my name"""
    if first_name == "":
        raise ValueError("enter first name")
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
