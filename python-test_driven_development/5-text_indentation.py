#!/usr/bin/python3


def text_indentation(text):
    if type(text) is not str:
        raise TypeError("text must be a string")
    carspecial = False
    for i in text:
        if i in [".", ":", "?"]:
            print(i)
            print()
            carspecial = True
        else:
            if carspecial and i == ' ':
                pass
            else:
                carspecial = False
                print(i, end="")
