#!/usr/bin/python3
"Unit tests for models/rectangle.py"
import unittest
from models.rectangle import Rectangle
from models.base import Base


class Test_init(unittest.TestCase):
    "Unit tests for models/rectangle.py"

    def test_is_base(self):
        self.assertIsInstance(Rectangle(10, 2), Base)
