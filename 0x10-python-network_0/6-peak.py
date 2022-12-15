#!/usr/bin/python3
"""Technical interview preparation:"""


def find_peak(list_of_integers):
    """function that finds a peak in a list"""
    li = list_of_integers
    if li == []:
        return None

    max = li[0]
    for i in li:
        if i > max:
            max = i
    return max
