#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argc = len(sys.argv)
    if argc == 2:
        print("1 argument:")
    elif argc == 1 or argc == 0:
        print("0 arguments.")
    else:
        print("{} arguments:".format(argc - 1))

    for i in range(1, len(sys.argv)):

        print("{}: {}".format(i, sys.argv[i]))
