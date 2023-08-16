#!/usr/bin/python3
# prints the result of the addition of all arguments
if __name__ == "__main__":
    from sys import argv
    res = 0
    for i in argv[1:]:
        res = res + int(i)
    print(res)
