#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new = my_list.copy()
    for num in range(len(new)):
        if new[num] == search:
            new[num] = replace
    return (new)
