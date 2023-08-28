#!/usr/bin/python3
# 4-list_division.py

def list_division(my_list_1, my_list_2, list_length):
    """
    list_division - divides elements in list 1 by element 2 lists

    Args:
    @my_list_1: the first list
    @my_list_2: the seond list
    @list_length: length of elements to be divided
    can be bigger than the length of both lists

    Return:
    new list (length = list_length) with all divisions

    Desc:
    If 2 elements can’t be divided, the division result should be equal to 0
    If an element is not an integer or float:
    print: wrong type
    If the division can’t be done (/0):
    print: division by 0
    If my_list_1 or my_list_2 is too short
    print: out of rangei
    """

