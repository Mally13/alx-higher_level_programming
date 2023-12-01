#!/usr/bin/python3
"""Finds a peak in a list of unsorted integers."""


def find_peak(list_of_integers):
    """Finds a peak in a list of unsorted integers."""
    peak = None
    if (len(list_of_integers) != 0):
        for i in range(len(list_of_integers) - 1):
            if (list_of_integers[i] >= list_of_integers[i - 1] and
                    list_of_integers[i] >= list_of_integers[i + 1]):
                if (peak is None or list_of_integers[i] > peak):
                    peak = list_of_integers[i]
    return peak
