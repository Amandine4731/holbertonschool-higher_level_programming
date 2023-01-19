#!/usr/bin/python3
import sys
argc = len(sys.argv)
if argc == 2:
    print("1 argument:")
else:
    print("{} arguments:".format(argc - 1))

for i in range(1, len(sys.argv)):

    print("{}: {}".format(i, sys.argv[i]))
