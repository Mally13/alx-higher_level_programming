#!/usr/bin/python3
# 8-multiple_returns.py

def multiple_returns(sentence):
    if (sentence == ''):
        return (0, None)
    slength = len(sentence)
    first = sentence[0]
    return (slength, first)
