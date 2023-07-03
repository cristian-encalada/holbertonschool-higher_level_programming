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


def test_initialization(self):
    """Test initialization of Rectangle object"""
    r1 = Rectangle(10, 10, 10, 10)
    self.assertEqual(str(r1), "[Rectangle] (1) 10/10 - 10/10")

    def test_inheritance(self):
        """Test if Rectangle is a subclass of Base"""
        self.assertIsInstance(Rectangle(10, 2), Base)

    def test_zero_args(self):
        """Test creation of Rectangle with zero arguments"""
        with self.assertRaises(TypeError):
            Rectangle()

    def test_only_one_arg(self):
        """Test creation of Rectangle with only one argument"""
        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_rectangles_ids(self):
        """Test if the IDs of two rectangles differ by 1"""
        r1 = Rectangle(8, 4)
        r2 = Rectangle(12, 6)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r2.id, 2)

    def test_four_args(self):
        """Test creation of Rectangle with four arguments"""
        r1 = Rectangle(8, 4, 0, 1)
        r2 = Rectangle(12, 6, 1, 2)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r2.id, 2)

    def test_five_args(self):
        """Test creation of Rectangle with five arguments"""
        r1 = Rectangle(8, 4, 0, 0, 7)
        r2 = Rectangle(12, 6, 1, 1, 8)
        self.assertEqual(r1.id, 7)
        self.assertEqual(r2.id, 8)


class TestRectangleAttr(unittest.TestCase):
    """Unit tests for Rectangle attributes validation"""

    def test_getters(self):
        """Test the getter methods"""
        r = Rectangle(2, 3, 4, 5)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 3)
        self.assertEqual(r.x, 4)
        self.assertEqual(r.y, 5)

    def test_attribute_access(self):
        """Test attribute access"""
        with self.assertRaises(AttributeError):
            rect = Rectangle(1, 2, 3, 4).__width
        with self.assertRaises(AttributeError):
            rect = Rectangle(1, 2, 3, 4).__height
        with self.assertRaises(AttributeError):
            rect = Rectangle(1, 2, 3, 4).__x
        with self.assertRaises(AttributeError):
            rect = Rectangle(1, 2, 3, 4).__y

    def test_attribute_types(self):
        """Test attribute types"""
        with self.assertRaises(TypeError):
            rect = Rectangle("test", 2)
        with self.assertRaises(TypeError):
            rect = Rectangle(1, "test2")
        with self.assertRaises(TypeError):
            rect = Rectangle(1, 2, "test3")
        with self.assertRaises(TypeError):
            rect = Rectangle(1, 2, 3, "test4")

    def test_attribute_values(self):
        """Test attribute values"""
        with self.assertRaises(ValueError):
            rect = Rectangle(0, 1)
        with self.assertRaises(ValueError):
            rect = Rectangle(1, 0)
        with self.assertRaises(ValueError):
            rect = Rectangle(1, 2, -1)
        with self.assertRaises(ValueError):
            rect = Rectangle(1, 2, 3, -1)

    def test_invalid_height(self):
        """Test creation of Rectangle with invalid height"""
        with self.assertRaises(TypeError) as cm:
            rect = Rectangle(10, "2")
        self.assertEqual(str(cm.exception), "height must be an integer")

    def test_invalid_width(self):
        """Test modification of Rectangle with invalid width"""
        r = Rectangle(10, 2)
        with self.assertRaises(ValueError) as cm:
            r.width = -10
        self.assertEqual(str(cm.exception), "width must be > 0")

    def test_invalid_x(self):
        """Test modification of Rectangle with invalid x"""
        r = Rectangle(10, 2)
        with self.assertRaises(TypeError) as cm:
            r.x = {}
        self.assertEqual(str(cm.exception), "x must be an integer")

    def test_invalid_y(self):
        """Test creation of Rectangle with invalid y"""
        with self.assertRaises(ValueError) as cm:
            rect = Rectangle(10, 2, 3, -1)
        self.assertEqual(str(cm.exception), "y must be >= 0")


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
