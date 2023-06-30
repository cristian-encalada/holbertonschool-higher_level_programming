#!/usr/bin/python3
"Task 1"
import unittest
from models.base import Base


class Test_init(unittest.TestCase):
    "Unit test for models/base.py"

    def test_id_right(self):
        base = Base(123)
        self.assertEqual(base.id, 123)
