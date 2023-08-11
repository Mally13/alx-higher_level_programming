#!/usr/bin/python3
for i in range(0, 10):
    for j in range(0, 10):
        if (i < j and j != i):
            print(f"{i}{j}", end=", " if i < 8 or j < 9 else "\n")
