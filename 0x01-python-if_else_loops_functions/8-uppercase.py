#!/usr/bin/python3
def uppercase(str):
    ustr = ""
    for i in str:
        j = 0
        if (ord(i) in range(97, 123)):
            j = ord(i) - 32
            ustr = ustr + chr(j)
        else:
            ustr = ustr + i
    print("{}".format(ustr))
