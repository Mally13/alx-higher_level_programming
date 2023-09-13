#!/usr/bin/python3
# 2-append_write.py

"""Defines a function that appends a string at the end of a text file
(UTF8) and returns the number of characters added"""


def append_write(filename="", text=""):
    """Appends a string to a text file and
    returns the number of characters added

    if g=file doesn't exist it creates a new one
    """
    with open(filename, 'a', encoding="utf-8") as file:
        return (file.write(text))
