#!/usr/bin/python3
# 1-my_list.py

"""Define a class MyList that inherits from list"""


class MyList(list):
    """class my list"""
    def __init__(self):
        """initialize list"""
        super().__init__()

    def print_sorted(self):
        """prints the list in an ascending sort"""
        print(sorted(self))
