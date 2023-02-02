#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_max(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_maxattheend(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_maxatthebeginning(self):
        self.assertEqual(max_integer([4, 2, 3, 1]), 4)

    def test_maxatthemiddle(self):
        self.assertEqual(max_integer([1, 4, 3, 2]), 4)

    def test_onenegnum(self):
        self.assertEqual(max_integer([1, 2, -3, 4]), 4)

    def test_onlynegnum(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_listofoneelement(self):
        self.assertEqual(max_integer([4]), 4)

    def test_listempty(self):
        self.assertEqual(max_integer(), None)
