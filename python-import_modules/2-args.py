#!/usr/bin/python3
if (__name__ == "__main__"):
    import sys
    args = len(sys.argv) - 1
    if (args == 0):
        print("0 arguments.")
    elif (args == 1):
        print("1 argument:")
        print("1:", sys.argv[1])
    elif (args > 0):
        print("{} arguments:".format(args))
        for i in range(1, args + 1):
            print("{}: {}".format(i, sys.argv[i]))
