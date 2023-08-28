#!/usr/bin/python3
# 3-safe_print_division.py

def safe_print_division(a, b):
    """
    safe_print_division - divides 2 integers and prints the result

    Args:
    @a: Int 1
    @b: Int 2

    Return:
    value of the divison or None
    """
    result = 0
    try:
        result = a / b
    except (ZeroDivisionError, TypeError):
        result = None
    finally:
        print("Inside result: {}".format(result))
    return (result)
