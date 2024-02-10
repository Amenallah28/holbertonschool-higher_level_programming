#!/usr/bin/python3
"""Write a function that returns True
if the object is exactly an instance
of the specifiedclass ; otherwise False."""


def is_same_class(obj, a_class):
    """ this is the function and it returns True or False"""
    if type(obj) is a_class:
        return True
    else:
        return False
