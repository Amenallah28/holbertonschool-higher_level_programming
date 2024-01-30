#!/usr/bin/python3
def print_last_digit(number):
    if (number < 0):
        number *= -1
    last_digt = number % 10
    print(last_digt, end="")
    return (last_digt)
