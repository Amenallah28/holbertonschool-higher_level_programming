#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new = a_dictionary.copy()
    for keyy, valuee in new.items():
        new[keyy] *= 2
    return (new)
