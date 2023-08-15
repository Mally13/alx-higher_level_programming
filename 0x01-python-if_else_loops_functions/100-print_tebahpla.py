#!/usr/bin/python3
originalrange = range(ord('a'), ord('z') + 1)
reversedrange = list(originalrange)[::-1]

for i in reversedrange:
    if (i % 2 != 0):
        i -= 32
    alph = chr(i)
    print(f"{alph}", end="")
