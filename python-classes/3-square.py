#!/usr/bin/python3
""" create a class named Square with control of size and return square area"""


class Square():
    """this is the square class"""

    def __init__(self, size=0):
        """display error message if the size is invalid"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """calculate the area of the square"""

        return (self.__size ** 2)
