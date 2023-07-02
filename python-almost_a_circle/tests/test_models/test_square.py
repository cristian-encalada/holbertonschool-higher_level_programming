#!/usr/bin/python3
"Unit tests for models/square.py"
from models.square import Square
from models.base import Base
from models.rectangle import Rectangle
import unittest


class Test_init(unittest.TestCase):
    "Unit tests for models/square.py"
    def test_is_subOf_Base(self):
        self.assertIsInstance(Square(5), Base)
