#!/usr/bin/python3
def __setattr__(self, attribute, firt_name):
    if not attribute in self.__dict__:
        print "Cannot set %s"
    else:
        self.__dict__[attribute] = first_name
