#!/usr/bin/python3
# 1-safe_print_integer.py

def safe_print_integer(value):
    """
    safe_print_integer: a function that prints an integer with "{:d}".format()
    Args:
    @value: can be any type (integer, string, etc.)
    
    Return:
    True if value has been correctly printed (it means the value is an integer)
    Otherwise, returns False
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        return (False)
