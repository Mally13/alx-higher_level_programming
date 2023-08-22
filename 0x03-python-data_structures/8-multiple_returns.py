#!/usr/bin/python3
# 8-multiple_returns.py

def multiple_returns(sentence):
    slength = len(sentence)
    if (slength == 0):
        return None
    first = sentence[0]
    stuple = (slength, first)
    return stuple

