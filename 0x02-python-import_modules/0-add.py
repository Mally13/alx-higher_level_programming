#!/usr/bin/python3
# 0_add.py
if __name__ == "__main__":
    """print sum of 1 and 2 """
    from add_0 import add
    a = 1
    b = 2
    print("{:n} + {:n} = {:n}".format(a, b, add(a, b)))
