#!/usr/bin/python3
''' Checking if the object belongs to a class'''


def inherits_from(obj, a_class):
    ''' Checking if the object belongs to a class'''
    return isinstance(obj, a_class) and type(obj) != a_class
