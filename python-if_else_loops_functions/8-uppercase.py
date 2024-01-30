#!/usr/bin/python3
def uppercase(str):
    string = ""
    for i in range(len(str)):
        if ((ord(str[i]) >= 97) and (ord(str[i]) <= 122)):
            string = string + (chr(ord(str[i]) - 32))
        else:
            string = string + (str[i])
    print(string)
