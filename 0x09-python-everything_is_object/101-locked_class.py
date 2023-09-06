#!/usr/bin/python3

"""Define class LockedClass with no class or object attribute that prevents
the user from dynamically creating new instance attributes, except if the new
instance attribute is called first_name.
"""


class LockedClass:
    """class LockedClass with no class or object attribute"""
    __slots__ = ('first_name',)

    def __init__(self):
        if hasattr(self, 'first_name'):
            self.first_name = None

    def __setattr__(self, name, value):
        if name == 'first_name':
            super().__setattr__(name, value)
        else:
            raise AttributeError(
                    f"'LockedClass' object has no attribute '{name}'")
