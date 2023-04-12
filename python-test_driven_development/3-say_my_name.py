#!/usr/bin/python3
"""module documentation"""


def say_my_name(first_name, last_name=""):
    """"function documentation"""
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    full_name = first_name + " " + last_name
    if last_name:
        print("My name is", full_name)
    else:
        print("My name is", first_name)
