#!/usr/bin/python3
def upperstringase(str):
    string = ""
    for i in str:
        if ((ord(i) >= 97) and (ord(i) <= 122)):
            string = string + chr(ord(i) - 32)
        else:
            string =string + i
    print("{}".format(string))
