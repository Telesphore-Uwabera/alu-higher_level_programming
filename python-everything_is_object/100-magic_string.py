#!/usr/bin/python3
def magic_string(n):
    result = ""
    for i in range(1, n+1):
        result += "BestSchool" * i
    return result
