#!/usr/bin/python3
# 100-my_int.py

"""Define a class MyInt that inherits from int"""


class MyInt(int):
    """Class MyInt that inherits int class"""
    def __eq__(self, other):
        """Inverts the behavior of the == operator"""
        return super().__ne__(other)

    def __ne__(self, other):
        """Inverts behavior of the != operator"""
        return super().__eq__(other)
