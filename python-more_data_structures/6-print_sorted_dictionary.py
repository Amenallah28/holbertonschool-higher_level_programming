#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for keyy, valuee in sorted(a_dictionary.items()):
        print("{}: {}".format(keyy, valuee))
