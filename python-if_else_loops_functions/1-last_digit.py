#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
n = number
last = str(number)[-1]
if (n >= 0):
    if (last == '6') or (last == '7') or (last == '8') or (last == '9'):
        print(f"Last digit of {number} is {last} and is greater than 5")
    elif (last == '5') or (last == '4') or (last == '3'):
        print(f"Last digit of {number} is {last} and is less than 6 and not 0")
    elif (last == '2') or (last == '1'):
        print(f"Last digit of {number} is {last} and is less than 6 and not 0")
    elif (last == '0'):
        print(f"Last digit of {number} is {last} and is 0")
else:
    print(f"Last digit of {number} is -{last} and is less than 6 and not 0")
