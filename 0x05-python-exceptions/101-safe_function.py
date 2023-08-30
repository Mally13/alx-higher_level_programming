#!/usr/bin/python3
# 101-safe_function.py
import sys
"""a function that executes a function safely"""


def safe_function(fct, *args):
    """Args:
    @fct: a ponter to a function
    @args:an array of pointers to function argumenta

    Return:
    Result of the functio or None
    """

    try:
        res = fct(*args)
        return (res)
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return None
