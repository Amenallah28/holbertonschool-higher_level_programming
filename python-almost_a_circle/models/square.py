#!/usr/bin/python3
"""Class Square that inherits from Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """constructor"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """returning info about this square"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """getter method width of the square"""
        return self.width

    @size.setter
    def size(self, size):
        """setter method: assign size to width and height"""
        self.width = size
        self.height = size

    def update2(self, id=None, size=None, x=None, y=None):
        """update instance attributes with args only"""
        if id is not None:
            self.id = id
        if size is not None:
            self.size = size
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        """update instance attributes with args and kwargs"""

        if args:
            self.update2(*args)
        elif kwargs:
            self.update2(**kwargs)

    def to_dictionary(self):
        """return the dictionary representation of a Square"""
        return {"id": self.id, "x": self.x, "size": self.size, "y": self.y}
