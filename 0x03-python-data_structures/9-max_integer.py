#!/usr/bin/python3
# 9-max_integer.py

def max_integer(my_list=[]):
    if (len(my_list) == 0):
        return None
    biggest = my_list[0]
    for i in my_list:
        if i > biggest:
            biggest = i
    return (biggest)
