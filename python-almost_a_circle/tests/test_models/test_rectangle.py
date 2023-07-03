#!/usr/bin/python3
"""Unit tests for Rectangle class"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
import pep8


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

    def test_width_getter(self):
        """Test the width getter method"""
        r = Rectangle(2, 2)
        self.assertEqual(r.width, 2)

    def test_height_getter(self):
        """Test the height getter method"""
        r = Rectangle(2, 3)
        self.assertEqual(r.height, 3)

    def test_x_getter(self):
        """Test the x getter method"""
        r = Rectangle(2, 2, 4)
        self.assertEqual(r.x, 4)

    def test_y_getter(self):
        """Test the y getter method"""
        r = Rectangle(2, 2, 4, 5)
        self.assertEqual(r.y, 5)

    def test_width_access(self):
        """Test access to width attribute"""
        with self.assertRaises(AttributeError):
            Rectangle(1, 2, 3, 4).__width

    def test_height_access(self):
        """Test access to height attribute"""
        with self.assertRaises(AttributeError):
            Rectangle(1, 2, 3, 4).__height

    def test_x_access(self):
        """Test access to x attribute"""
        with self.assertRaises(AttributeError):
            Rectangle(1, 2, 3, 4).__x

    def test_y_access(self):
        """Test access to y attribute"""
        with self.assertRaises(AttributeError):
            Rectangle(1, 2, 3, 4).__y

    def test_width_not_int(self):
        """Test width not being an integer"""
        with self.assertRaises(TypeError):
            rect = Rectangle("test", 2)

    def test_height_not_int(self):
        """Test height not being an integer"""
        with self.assertRaises(TypeError):
            rect = Rectangle(1, "test2")

    def test_x_not_int(self):
        """Test x not being an integer"""
        with self.assertRaises(TypeError):
            rect = Rectangle(1, 2, "test3")

    def test_y_not_int(self):
        """Test y not being an integer"""
        with self.assertRaises(TypeError):
            rect = Rectangle(1, 2, 3, "test4")

    def test_width_under_equal_0(self):
        """Test width being under or equal to 0"""
        with self.assertRaises(ValueError):
            rect = Rectangle(0, 1)

    def test_height_under_equal_0(self):
        """Test height being under or equal to 0"""
        with self.assertRaises(ValueError):
            rect = Rectangle(1, 0)

    def test_x_under_0(self):
        """Test x being under 0"""
        with self.assertRaises(ValueError):
            rect = Rectangle(1, 2, -1)

    def test_y_under_0(self):
        """Test y being under 0"""
        with self.assertRaises(ValueError):
            rect = Rectangle(1, 2, 3, -1)

    def test_invalid_height(self):
        """Test creation of Rectangle with invalid height"""
        with self.assertRaises(TypeError) as cm:
            Rectangle(10, "2")
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
            Rectangle(10, 2, 3, -1)
        self.assertEqual(str(cm.exception), "y must be >= 0")


class TestRectangleArea(unittest.TestCase):
    """Unit tests for Area meathod of Rectangle"""

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


class TestRectangleDisplay(unittest.TestCase):
    """Unit tests for display meathod of Rectangle"""

    def test_display_with_arg(self):
        """Test display method with an argument"""
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 4).display(2)

    def test_update(self):
        """Test update method of Rectangle object"""
        r3 = Rectangle(10, 10, 10, 10)
        self.assertEqual(str(r3), "[Rectangle] (26) 10/10 - 10/10")

        r3.update(height=1)
        self.assertEqual(str(r3), "[Rectangle] (26) 10/10 - 10/1")

        r3.update(width=1, x=2)
        self.assertEqual(str(r3), "[Rectangle] (26) 2/10 - 1/1")

        r3.update(y=1, width=2, x=3, id=89)
        self.assertEqual(str(r3), "[Rectangle] (89) 3/1 - 2/1")

        r3.update(x=1, height=2, y=3, width=4)
        self.assertEqual(str(r3), "[Rectangle] (89) 1/3 - 4/2")

    def test_update_kw(self):
        """Test the update method of Rectangle with keyword arguments"""
        r = Rectangle(1, 1)
        r.update(id=11, height=12, width=13, y=9, x=15)
        self.assertEqual(r.id, 11)
        self.assertEqual(r.height, 12)
        self.assertEqual(r.width, 13)
        self.assertEqual(r.y, 9)
        self.assertEqual(r.x, 15)


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
