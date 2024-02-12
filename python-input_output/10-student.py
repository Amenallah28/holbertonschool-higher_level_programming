#!/usr/bin/python3
"""Write a class Student that defines a student"""


class Student:
    """this is the class Student"""

    def __init__(self, first_name, last_name, age):
        """initialize first_name ,last_name and age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    
    def to_json(self, attrs=None):
        """ retrieves a dictionary representation of a Student instance
        If attrs is a list of strings, only attribute names contained in this 
        list must be retrieved.
        Otherwise, all attributes must be retrieved
        """
        if isinstance(attrs, list) and all(isinstance(el, attrs) for el in attrs):
            return 
        else:
            return self.__dict__
