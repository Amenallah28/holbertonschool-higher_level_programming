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
