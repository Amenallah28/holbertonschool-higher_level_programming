#!/usr/bin/python3
"""create a class named Square and return the square area"""


class Square():
    """this is a square class"""

    def __init__(self, size=0):
        """initialize size"""
        self.__size = size

    @property
    def size(self):
        """retrieve size"""
        return self.__size

    @size.setter
    def size(self, value):
        """set value to size otherwise display error message"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """calculate the area of the square"""
        return self.__size ** 2
