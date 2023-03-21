#!/usr/bin/python3
def lookup(obj):
    """
    Return a list of attributes and methods for the given object.
    """
    return [attr for attr in dir(obj) if not attr.startswith("__")]
