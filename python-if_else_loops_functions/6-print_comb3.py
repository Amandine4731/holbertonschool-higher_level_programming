#!/usr/bin/python3
for dizaine in range(0, 9 + 1):
    for unité in range(dizaine + 1, 9 + 1):
        if (dizaine == 8) and (unité == 9):
            print("89")
        else:
            print("{:d}{:d}".format(dizaine, unité), end=", ")
