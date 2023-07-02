import unittest
from models.square import Square
from models.base import Base
import pep8


class TestSquare(unittest.TestCase):
    """Unit tests for the Square class"""

    def test_inheritance(self):
        """Test if Square is a subclass of Base"""
        self.assertIsInstance(Square(10), Base)

    def test_zero_args(self):
        """Test creation of Square with zero arguments"""
        with self.assertRaises(TypeError):
            Square()

    def test_only_one_arg(self):
        """Test creation of Square with only one argument"""
        square = Square(5)
        self.assertEqual(square.size, 5)
        self.assertEqual(square.x, 0)
        self.assertEqual(square.y, 0)
        self.assertNotEqual(square.id, None)

    def test_two_args(self):
        """Test creation of Square with two arguments"""
        square = Square(5, 2)
        self.assertEqual(square.size, 5)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 0)
        self.assertNotEqual(square.id, None)

    def test_three_args(self):
        """Test creation of Square with three arguments"""
        square = Square(5, 2, 3)
        self.assertEqual(square.size, 5)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)
        self.assertNotEqual(square.id, None)

    def test_four_args(self):
        """Test creation of Square with four arguments"""
        square = Square(5, 2, 3, 4)
        self.assertEqual(square.size, 5)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)
        self.assertEqual(square.id, 4)

    def test_size_getter(self):
        """Test the size getter method"""
        square = Square(5)
        self.assertEqual(square.size, 5)

    def test_size_setter(self):
        """Test the size setter method"""
        square = Square(5)
        square.size = 10
        self.assertEqual(square.size, 10)

    def test_x_getter(self):
        """Test the x getter method"""
        square = Square(5, 2)
        self.assertEqual(square.x, 2)

    def test_x_setter(self):
        """Test the x setter method"""
        square = Square(5, 2)
        square.x = 10
        self.assertEqual(square.x, 10)

    def test_y_getter(self):
        """Test the y getter method"""
        square = Square(5, 2, 3)
        self.assertEqual(square.y, 3)

    def test_y_setter(self):
        """Test the y setter method"""
        square = Square(5, 2, 3)
        square.y = 10
        self.assertEqual(square.y, 10)

    def test_area(self):
        """Test the area method of Square"""
        square = Square(5)
        self.assertEqual(square.area(), 25)

    def test_str(self):
        """Test the __str__ method of Square"""
        square = Square(5, 2, 3, 4)
        expected_output = "[Square] (4) 2/3 - 5"
        self.assertEqual(str(square), expected_output)

    def test_update_args(self):
        """Test the update method of Square with *args"""
        square = Square(5, 2, 3, 4)
        square.update(10, 7, 8, 9)
        self.assertEqual(square.id, 10)
        self.assertEqual(square.size, 7)
        self.assertEqual(square.x, 8)
        self.assertEqual(square.y, 9)

    def test_update_kwargs(self):
        """Test the update method of Square with **kwargs"""
        square = Square(5, 2, 3, 4)
        square.update(id=10, size=7, x=8, y=9)
        self.assertEqual(square.id, 10)
        self.assertEqual(square.size, 7)
        self.assertEqual(square.x, 8)
        self.assertEqual(square.y, 9)

    def test_to_dictionary(self):
        """Test the to_dictionary method of Square"""
        square = Square(5, 2, 3, 4)
        expected_dict = {'id': 4, 'size': 5, 'x': 2, 'y': 3}
        self.assertEqual(square.to_dictionary(), expected_dict)

    def test_pep8_square(self):
        """Test PEP8 style for models/square.py"""
        p8 = pep8.StyleGuide(quiet=True)
        p = p8.check_files(['models/square.py'])
        self.assertEqual(p.total_errors, 0, "Fix PEP8 issues in square.py")

    def test_pep8_test_square(self):
        """Test PEP8 style for tests/test_models/test_square.py"""
        p8 = pep8.StyleGuide(quiet=True)
        p = p8.check_files(['tests/test_models/test_square.py'])
        self.assertEqual(p.total_errors, 0, "Fix PEP8 in test_square.py")


if __name__ == '__main__':
    unittest.main()
