#!/usr/bin/python3
from calculator_1 import calculator
if __name__ == "__main__":
    a = 10
    b = 5
print("{} + {} = {}".format(a, b, add(a, b)))
print("{} - {} = {}".format(a, b, subtract(a, b)))
print("{} / {} = {}".format(a, b, divide(a, b)))
print("{} * {} = {}".format(a, b, multiply(a, b)))
