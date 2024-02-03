#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    list1 = []
    for i in matrix:
        list1.append(list(map(lambda x: x**2, i)))
    return list1
