#!/usr/bin/python3
def best_score(a_dictionary):
    for key, value in sorted(a_dictionary.items(), reverse=True):
        print("Best score: {}".format(key))
