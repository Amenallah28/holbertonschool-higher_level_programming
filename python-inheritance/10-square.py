#!/usr/bin/python3
"""Write a class Square that inherits from Rectangle"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """this is the square class"""

    def __init__(self, size):
        """ initialize size"""
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """calculate the area of the square"""
        return self.__size ** 2
