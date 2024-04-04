#!/usr/bin/python3
def roman_to_int(roman_string):
    roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    s = 0
    prev = 0
    for i in roman_string[::-1]:
        value = roman.get(i, 0)
        if value == 0:
            return 0
        if roman[i] >= prev:
            s += roman[i]
        else:
            s -= roman[i]
        prev = roman[i]
    return s
