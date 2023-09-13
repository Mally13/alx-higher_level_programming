#!/usr/bin/python3
# 1-write_file.py

"""
Defines a function that writes a string to a text file (UTF8)
and returns the number of characters written
"""


def write_file(filename="", text=""):
    """writes string to text file(UTF8) and returns chars written"""
    try:
        with open(filename, 'w', encoding="utf-8") as file:
            chars = file.write(text)
            return (chars)
    except PermissonError:
        print(f"Permission denied: Cannot write file '{filename}'")
    except Exception as e:
        print(f"An error occurred: {e}")
