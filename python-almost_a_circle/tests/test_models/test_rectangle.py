#!/usr/bin/python3
"""Unit tests for Rectangle class"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
import pep8
import sys
from io import StringIO


class TestRectangleInit(unittest.TestCase):
    """Unit tests for Rectangle class initialization"""


def test_id(self):
    """Test initialization of Rectangle object"""
    Base._Base__nb_objects = 0
    r1 = Rectangle(10, 2)
    self.assertIsNotNone(id(r1))

    def test_instance(self):
        """Test if Rectangle is instace of Base"""
    Base._Base__nb_objects = 0
    r2 = Rectangle(2, 10)
    self.assertIsInstance(r2, Rectangle)

    def test_numObj(self):
        """Test correct number of objects"""
        Base._Base__nb_objects = 0
        r3 = Rectangle(10, 2, 0, 0)
        r4 = Rectangle(5, 5)
        self.assertEqual(r4.id, 2)


class TestRectangleAttr(unittest.TestCase):
    """Unit tests for Rectangle attributes validation"""

    def test_getterAndSetter(self):
        """checks getter and setter"""
        Base._Base__nb_objects = 0
        r5 = Rectangle(10, 2, 0, 0)
        self.assertEqual(r5.width, 10)
        self.assertEqual(r5.height, 2)
        self.assertEqual(r5.x, 0)
        self.assertEqual(r5.y, 0)

    def test_errors(self):
        """checks invalid attributes"""
        Base._Base__nb_objects = 0
        r = Rectangle(10, 2)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.width = "2"
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.width = -10
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.height = "2"
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.height = -10
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.x = {}
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(10, 2, -3, 1)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r.y = {}
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(10, 2, 3, -1)


class TestRectangleMethods(unittest.TestCase):
    """Unit tests for methods of Rectangle"""

    def test_area(self):
        """Test the area method of Rectangle"""
        r = Rectangle(10, 10)
        self.assertEqual(r.area(), 100)

    def test_area_five_args(self):
        """Test the area method with five arguments"""
        r = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r.area(), 56)

    def test_area_with_arg(self):
        """Test area method with a wrong argument"""
        with self.assertRaises(TypeError):
            Rectangle(1, 2).area(42)

    def test_display(self):
        """Test display method with two arguments"""
        Base._Base__nb_objects = 0
        r7 = Rectangle(4, 6)
        old_stdout = sys.stdout
        result = StringIO()
        sys.stdout = result
        r7.display()
        sys.stdout = old_stdout
        result_string = result.getvalue()
        self.assertEqual(result_string,
                         "####\n####\n####\n####\n####\n####\n")

    def test_str(self):
        """Test str method"""
        Base._Base__nb_objects = 0
        r8 = Rectangle(4, 6, 2, 1, 12)
        r9 = Rectangle(5, 5, 1)
        string1 = r8.__str__()
        string2 = r9.__str__()
        self.assertEqual(string1,
                         "[Rectangle] (12) 2/1 - 4/6")
        self.assertEqual(string2,
                         "[Rectangle] (1) 1/0 - 5/5")

    def test_display_xy(self):
        """Test display method with four arguments"""
        Base._Base__nb_objects = 0
        r1 = Rectangle(2, 3, 2, 2)
        old_stdout = sys.stdout
        result = StringIO()
        sys.stdout = result
        r1.display()
        sys.stdout = old_stdout
        result_string = result.getvalue()
        self.assertEqual(result_string, "\n\n  ##\n  ##\n  ##\n")
        r2 = Rectangle(3, 2, 1, 0)
        old_stdout = sys.stdout
        result = StringIO()
        sys.stdout = result
        r2.display()
        sys.stdout = old_stdout
        result_string = result.getvalue()
        self.assertEqual(result_string, " ###\n ###\n")

    def test_display_with_arg(self):
        """Test display method with an argument"""
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 4).display(2)

    def test_update(self):
        """Test update method of Rectangle object"""
        r3 = Rectangle(10, 10, 10, 10)
        self.assertEqual(str(r3), "[Rectangle] (2) 10/10 - 10/10")
        r3.update(height=1)
        self.assertEqual(str(r3), "[Rectangle] (2) 10/10 - 10/1")
        r3.update(width=1, x=2)
        self.assertEqual(str(r3), "[Rectangle] (2) 2/10 - 1/1")
        r3.update(y=1, width=2, x=3, id=89)
        self.assertEqual(str(r3), "[Rectangle] (89) 3/1 - 2/1")
        r3.update(x=1, height=2, y=3, width=4)
        self.assertEqual(str(r3), "[Rectangle] (89) 1/3 - 4/2")

    def test_update_kwargs(self):
        """Test the update method of Rectangle with keyword arguments"""
        Base._Base__nb_objects = 0
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(height=1)
        string = r1.__str__()
        self.assertEqual(string, "[Rectangle] (1) 10/10 - 10/1")
        r1.update(width=1, x=2)
        string = r1.__str__()
        self.assertEqual(string, "[Rectangle] (1) 2/10 - 1/1")
        r1.update(y=1, width=2, x=3, id=89)
        string = r1.__str__()
        self.assertEqual(string, "[Rectangle] (89) 3/1 - 2/1")
        r1.update(x=1, height=2, y=3, width=4)
        string = r1.__str__()
        self.assertEqual(string, "[Rectangle] (89) 1/3 - 4/2")


class TestRectanglePEP8(unittest.TestCase):
    """Unit tests for Rectangle class PEP8 style"""

    def test_pep8_rect(self):
        """Test PEP8 style for models/rectangle.py"""
        p8 = pep8.StyleGuide(quiet=True)
        p = p8.check_files(['models/rectangle.py'])
        self.assertEqual(p.total_errors, 0, "Fix PEP8 issues in rectangle.py")

    def test_pep8_test_rect(self):
        """Test PEP8 style for tests/test_models/test_rectangle.py"""
        p8 = pep8.StyleGuide(quiet=True)
        p = p8.check_files(['tests/test_models/test_rectangle.py'])
        self.assertEqual(p.total_errors, 0, "Fix PEP8 in test_rectangle.py")


if __name__ == '__main__':
    unittest.main()
