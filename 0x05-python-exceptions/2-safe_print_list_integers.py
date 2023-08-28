#!/usr/bin/python3
# 2-safe_print_list_integers.py

def safe_print_list_integers(my_list=[], x=0):
    """
    safe_print_list_integers - prints the first x elements of
    a list and only integers
    Args:
    @my_list: a list that can contain any type (integer, string, etc.)
    @x: represents the number of elements to access in my_list

    Return:
    real number of integers printed
    """
    no_int_printed = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end = "")
            no_int_printed += 1
        except (TypeError, ValueError):
            no_int_printed += 0
    print("")
    return (no_int_printed)
