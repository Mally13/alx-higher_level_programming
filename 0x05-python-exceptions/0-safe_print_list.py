#!/usr/bin/python3
# 0-safe_print_list.py

def safe_print_list(my_list=[], x=0):
    """prints x elements of a list
    Args:
    @my_list: list that can contain any type (integer, string, etc.)
    @x: represents the number of elements to print
    Returns:
    The number of elements printed
    """
    no_printed = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            no_printed += 1
        except IndexError:
            break
    print("")
    return (no_printed)
