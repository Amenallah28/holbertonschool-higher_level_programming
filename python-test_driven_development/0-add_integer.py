#!/usr/bin/python3
"""

a function that adds 2 integers.
"""


def add_integer(a, b=98):
    """
    Parameters:
    a (int or float): The first number to be added.
    b (int or float, optional): The second number to be added. Defaults to 98.

    Returns:
    int: The sum of 'a' and 'b', converted to an integer.

    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
