#!/usr/bin/python3
# 100-safe_print_integer_err.py
import sys
"""a function that prints an integer"""


def safe_print_integer_err(value):
    """Args:
    @value: can be any type
    Return:
    True if int is printed otherwise false
    """

    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError):
        print("Exception: Unknown format code 'd' for object of type '{}'".
              format(value.__class__.__name__), file=sys.stderr)
        return False
