#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        if (97 <= ord(str[i]) <= 122):
            c = chr(ord(str[i]) - 32)
        else:
            c = str[i]
        print("{}".format(c), end="")
    print(c)
