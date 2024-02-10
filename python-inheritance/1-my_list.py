#!/usr/bin/python3
"""Write a class MyList that inherits from list"""


class MyList(list):
    """this the class MyList"""

    def print_sorted(self):
        """print the list sorted in ascending order"""
        print(sorted(self))
