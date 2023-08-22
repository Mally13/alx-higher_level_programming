#!/usr/bin/python3
# 5-no_c.py

def no_c(my_string):
    str_noc = []
    for ch in my_string:
        if (ch != 'C' and ch != 'c'):
            str_noc.append(ch)
    return ''.join(str_noc)
