#!/usr/bin/python3
def upperstringase(str):
    string = ""
    for i in str:
        if ((ord(i) >= 97) and (ord(i) <= 122)):
            string += chr(ord(i) - 32)
        else:
            string += i
    print("{}".format(string))
