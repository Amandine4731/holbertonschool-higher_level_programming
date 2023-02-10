#!/usr/bin/python3
"""
    Python program
"""


import json

def class_to_json(obj):
    """  return the dictionary description with simple data structure """
    return json.dumps(obj.__dict__)
