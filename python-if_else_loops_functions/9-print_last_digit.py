#!/usr/bin/python3
def print_last_digit(number):
    last = number % 10
    lastneg = number % (-10)

    if (number >= 0):
        print(last, end="")

    else:
        print(lastneg * (-1), end="")

    return lastneg * (-1)
    print("")
