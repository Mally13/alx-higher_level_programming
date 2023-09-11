#!/usr/bin/python3
# 1-my_list.py

"""Define a class MyList that inherits from list"""


class MyList(list):
    """class MyList that inherits from list"""
    def __init__(self, *args):
        super().__init__(*args)
    
    def print_sorted(self):
        """prints the list in an ascending sort"""
        print(sorted(self))
