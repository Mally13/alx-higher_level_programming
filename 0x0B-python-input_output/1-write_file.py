#!/usr/bin/python3
# 1-write_file.py

"""
Defines a function that writes a string to a text file (UTF8)
and returns the number of characters written
"""


def write_file(filename="", text=""):
    """writes string to text file(UTF8) and returns chars written"""
    with open(filename, 'w', encoding="utf-8") as file:
        return(file.write(text))
