#!/usr/bin/python3
"""Unit tests for models/base.py class"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Test class for Base class"""

    def test_new_instances_with_id(self):
        """New instances with id"""
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b3 = Base()
        self.assertEqual(b3.id, 3)
        b4 = Base(12)
        self.assertEqual(b4.id, 12)
        b5 = Base()
        self.assertEqual(b5.id, 4)


if __name__ == '__main__':
    unittest.main()
