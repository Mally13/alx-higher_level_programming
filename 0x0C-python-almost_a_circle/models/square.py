#!/usr/bin/python3
# square.py

"""Defines class Square that inherits from Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    class Square that inherits from Rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        """initializes a Square"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter for size"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for size that assigns the same value to width and height"""
        self.width = value
        self.height = value

    def __str__(self):
        """Returns [Square] (<id>) <x>/<y> - <size>"""
        sq_str = f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
        return (sq_str)

    def update(self, *args, **kwargs):
        """assigns an argument to each new attribute"""
        if args and len(args) != 0:
            num_args = len(args)
            if num_args >= 1:
                self.id = args[0]
            if num_args >= 2:
                self.width = args[1]
                self.height = args[1]
            if num_args >= 3:
                self.x = args[2]
            if num_args >= 4:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)
