#!/usr/bin/python3
"""Unit tests for Rectangle class"""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Unit tests for Rectangle class"""


def test_initialization(self):
    """Test initialization of Rectangle object"""
    r1 = Rectangle(10, 10, 10, 10)
    self.assertEqual(str(r1), "[Rectangle] (1) 10/10 - 10/10")


def test_update(self):
    """Test update method of Rectangle object"""
    r1 = Rectangle(10, 10, 10, 10)

    r1.update(1, 2, 3, 4, 5)
    self.assertEqual(str(r1), "[Rectangle] (1) 4/5 - 2/3")

    r1.update(height=1)
    self.assertEqual(str(r1), "[Rectangle] (1) 4/5 - 2/1")

    r1.update(width=1, x=2)
    self.assertEqual(str(r1), "[Rectangle] (1) 2/5 - 1/1")

    r1.update(y=1, width=2, x=3, id=89)
    self.assertEqual(str(r1), "[Rectangle] (89) 3/1 - 2/1")

    r1.update(x=1, height=2, y=3, width=4)
    self.assertEqual(str(r1), "[Rectangle] (89) 1/3 - 4/2")


class TestRectangle(unittest.TestCase):
    """Unit tests for the Rectangle class"""

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
        rect = Rectangle(8, 4)
        angle = Rectangle(12, 6)
        self.assertEqual(rect.id, angle.id - 1)

    def test_four_args(self):
        """Test creation of Rectangle with four arguments"""
        rect = Rectangle(8, 4, 0, 1)
        angle = Rectangle(12, 6, 1, 2)
        self.assertEqual(rect.id, angle.id - 1)

    def test_five_args(self):
        """Test creation of Rectangle with five arguments"""
        rect = Rectangle(8, 4, 0, 0, 7)
        angle = Rectangle(12, 6, 1, 1, 8)
        self.assertEqual(rect.id, 7)

    def test_width_getter(self):
        """Test the width getter method"""
        rect = Rectangle(2, 2)
        self.assertEqual(rect.width, 2)

    def test_height_getter(self):
        """Test the height getter method"""
        rect = Rectangle(2, 3)
        self.assertEqual(rect.height, 3)

    def test_x_getter(self):
        """Test the x getter method"""
        rect = Rectangle(2, 2, 4)
        self.assertEqual(rect.x, 4)

    def test_y_getter(self):
        """Test the y getter method"""
        rect = Rectangle(2, 2, 4, 5)
        self.assertEqual(rect.y, 5)

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
            rect = Rectangle("Jon", 2)

    def test_height_not_int(self):
        """Test height not being an integer"""
        with self.assertRaises(TypeError):
            rect = Rectangle(1, "Snow")

    def test_x_not_int(self):
        """Test x not being an integer"""
        with self.assertRaises(TypeError):
            rect = Rectangle(1, 2, "Winterfell")

    def test_y_not_int(self):
        """Test y not being an integer"""
        with self.assertRaises(TypeError):
            rect = Rectangle(1, 2, 3, "RedWedding")

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

    def test_area(self):
        """Test the area method of Rectangle"""
        rect = Rectangle(10, 10)
        self.assertEqual(rect.area(), 100)

    def test_area_with_arg(self):
        """Test area method with an argument"""
        with self.assertRaises(TypeError):
            Rectangle(1, 2).area(42)

    def test_display_with_arg(self):
        """Test display method with an argument"""
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 4).display(2)

    def test_update_kw(self):
        """Test the update method of Rectangle with keyword arguments"""
        r = Rectangle(1, 1)
        r.update(id=11, height=12, width=13, y=9, x=15)
        self.assertEqual(r.id, 11)
        self.assertEqual(r.height, 12)
        self.assertEqual(r.width, 13)
        self.assertEqual(r.y, 9)
        self.assertEqual(r.x, 15)


if __name__ == '__main__':
    unittest.main()
