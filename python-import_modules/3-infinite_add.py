#!/usr/bin/py#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    if len(argv) <= 1:
        print("{}".format(len(argv)-1))
    else:
        sum = 0
        for i in range(1, len(argv)):
            sum += int(argv[i])
        print("{}".format(sum))
        