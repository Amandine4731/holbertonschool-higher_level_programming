#!/usr/bin/python3
for numbers in range(0, 99 + 1):
    if numbers <= 9:
        print("0{:d}".format(numbers), end=", ")
    else:
        print("{:d}".format(numbers), end=", " if numbers < 99 else "\n")
