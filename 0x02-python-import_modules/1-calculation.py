#!/usr/bin/python3
# A program that does some maths and prints results
# 1-calculation.py


"""Performs math then prints the result"""
from calculator_1 import add, sub, mul, div

a = 10
b = 5

print("{} + {} = {}".format(a, b, add(a, b)))
print("{} - {} = {}".format(a, b, sub(a, b)))
print("{} * {} = {}".format(a, b, mul(a, b)))
print("{} / {} = {}".format(a, b, div(a, b)))
