#!/usr/bin/python3
"Unit tests for models/base.py"
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class Test_init(unittest.TestCase):
    "Unit tests for models/base.py"

    def test_id_right(self):
        base = Base(123)
        self.assertEqual(base.id, 123)
