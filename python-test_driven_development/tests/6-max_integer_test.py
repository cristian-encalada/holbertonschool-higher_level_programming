#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    "Unittest for max_integer"
    def test_ascending(self):
        self.assertEqual(max_integer([0, 1, 2, 3]), 3)

    def test_descending(self):
        self.assertEqual(max_integer([3, 2, 1, 0]), 3)

    def test_all_zero(self):
        self.assertEqual(max_integer([0, 0, 0, 0]), 0)

    def test_negatives(self):
        self.assertEqual(max_integer([-5, -8, -1, -4]), -1)

    def test_mixed(self):
        self.assertEqual(max_integer([-5, -8, -1, 14]), 14)

    def test_chars(self):
        self.assertEqual(max_integer(['w', 'x', 'y', 'z']), 'z')

    def test_empty(self):
        self.assertEqual(max_integer([]), None)

    def test_inf(self):
        self.assertEqual(max_integer([5, float("inf")]), float("inf"))

    def test_one_element(self):
        self.assertEqual(max_integer([8]), 8)

    def test_string(self):
        with self.assertRaises(TypeError):
            max_integer([1, 2, "test"])

    def test_more_args(self):
        with self.assertRaises(TypeError):
            max_integer([5, 8, "test"], 5)


if __name__ == "__main__":
    unittest.main()
