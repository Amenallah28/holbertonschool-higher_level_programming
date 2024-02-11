#!/usr/bin/python3
"""Write a class BaseGeometry with 2 public instance methods"""


class BaseGeometry:
    """ this is the class"""

    def area(self):
        """this is the first public instnace method"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """this is the second public instance method"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))