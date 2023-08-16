#!/usr/bin/python3
# handles basic math operations

if __name__ == "__main__":
    from sys import argv, exit
    from calculator_1 import add, sub, mul, div

    operations = {'+': add, '-': sub, '/': div, '*': mul}
    res = 0
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    elif argv[2] not in list(operations.keys()):
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    else:
        res = operations[argv[2]](int(argv[1]), int(argv[3]))
        print("{} {} {} = {}".format(argv[1], argv[2], argv[3], res))
        exit(0)
