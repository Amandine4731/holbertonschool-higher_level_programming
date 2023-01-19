#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add as cal_add
    a = 10
    b = 5
    print("{} + {} = {}".format(a, b, cal_add(a, b)))

    from calculator_1 import sub as cal_sub
    print("{} - {} = {}".format(a, b, cal_sub(a, b)))

    from calculator_1 import mul as cal_mul
    print("{} * {} = {}".format(a, b, cal_mul(a, b)))

    from calculator_1 import div as cal_div
    print("{} / {} = {}".format(a, b, cal_div(a, b)))
