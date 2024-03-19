#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list is None or len(my_list) == 0:
        return None
    elif len(my_list) == 1:
        return my_list[0]
    else:
        result = my_list[0]
        for max in range(0, len(my_list) - 1):
            if result < my_list[max + 1]:
                result = my_list[max + 1]
        return result
