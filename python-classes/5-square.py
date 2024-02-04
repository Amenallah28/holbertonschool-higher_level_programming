#!/usr/bin/python3
""" create a class square and return the square area and print it with #"""


class Square:
    """this is a class named square"""

    def __init__(self, size=0):
        """initialize size"""
        self.__size = size

    @property
    def size(self):
        """get the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """display error msg if the value is invalid"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """calculate the area of the square"""
        return self.__size ** 2

    def my_print(self):
        """print the square with #"""
        if self.__size == 0:
            print()
        else:
            for row in range(self.__size):
                for col in range(self.__size):
                    print("#", end="")
                print()
