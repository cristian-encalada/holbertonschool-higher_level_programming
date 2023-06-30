#!/usr/bin/python3
"""Unit tests for base.py"""
import unittest
from models.base import Base


class TestBase_Instantiation(unittest.TestCase):
    """Unit tests for Base class"""
    def test_id_no_duplicates(self):
        """ Verify that there are no duplicate values for id"""
        Base._Base__nb_objects = 0
        b1 = Base()
        b2 = Base()
        b3 = Base()
        b4 = Base(12)
        b5 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)
        self.assertEqual(b4.id, 12)
        self.assertEqual(b5.id, 4)


if __name__ == "__main__":
    unittest.main()
