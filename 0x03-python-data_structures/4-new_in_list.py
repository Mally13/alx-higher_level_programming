#!/usr/bin/python3
# 4-new_in_list.py

def new_in_list(my_list, idx, element):
    if isinstance(my_list, list):
        if idx < 0:
            return mylist
        elif idx > (len(my_list) - 1):
            return my_list
        else:
            new_list = my_list.copy()
            new_list[idx] = element
            return new_list
