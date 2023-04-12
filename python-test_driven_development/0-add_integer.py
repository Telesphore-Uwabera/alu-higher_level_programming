#!/usr/bin/python3
"""Add two numbers a and b by using python codes"""


def add_integer(a, b=98):
    """
    return- sum of a and b
        a: int or float
        b: int or float, default 98
    """
    if type(a) == float or type(b) == float:
        a = int(a)
        b = int(b)

    if type(a) != int:
        raise TypeError("a must be an integer")
    if type(b) != int:
        raise TypeError("b must be an integer")

    return a + b
