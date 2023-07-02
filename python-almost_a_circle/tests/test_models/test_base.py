#!/usr/bin/python3
"""Unit tests for models/base.py class"""
import unittest
from models.base import Base


class TestBaseInit(unittest.TestCase):
    """Unit tests for Base class initialization"""

    def test_id_valid(self):
        """Test initialization with valid id"""
        base = Base(222)
        self.assertEqual(base.id, 222)

    def test_id_3times(self):
        """Test initialization of multiple instances"""
        base1 = Base()
        self.assertEqual(base1.id, 1)
        base2 = Base(15)
        self.assertEqual(base2.id, 15)
        base3 = Base()
        self.assertEqual(base3.id, 2)

    def test_id(self):
        """Test initialization with positive id"""
        b = Base(50)
        self.assertEqual(50, b.id)

    def test_id_zero(self):
        """Test initialization with id 0"""
        b = Base(0)
        self.assertEqual(0, b.id)

    def test_id_negative(self):
        """Test initialization with negative id"""
        b = Base(-20)
        self.assertEqual(-20, b.id)

    def test_id_string(self):
        """Test initialization with id as string"""
        b = Base("str")
        self.assertEqual("str", b.id)

    def test_id_list(self):
        """Test initialization with id as list"""
        b = Base([1, 2, 3])
        self.assertEqual([1, 2, 3], b.id)

    def test_id_dict(self):
        """Test initialization with id as dictionary"""
        b = Base({"id": 100})
        self.assertEqual({"id": 100}, b.id)

    def test_id_tuple(self):
        """Test initialization with id as tuple"""
        b = Base((8,))
        self.assertEqual((8,), b.id)


if __name__ == '__main__':
    unittest.main()
