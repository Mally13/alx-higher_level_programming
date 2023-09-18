"""Defines unittests for models/rectangle.py."""
import io
import sys
from unittest.mock import patch
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):

    def test_constructor_with_valid_values(self):
        r = Rectangle(5, 10, 2, 3, 1)
        self.assertEqual(r.width, 5)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 2)
        self.assertEqual(r.y, 3)
        self.assertEqual(r.id, 1)

    def test_constructor_with_invalid_values(self):
        with self.assertRaises(ValueError):
            Rectangle(-5, 10, 2, 3, 1)

    def test_area_calculation(self):
        r = Rectangle(5, 10, 2, 3, 1)
        self.assertEqual(r.area(), 50)

    def test_display(self):
        r = Rectangle(3, 2, 1, 1, 1)
        expected_output = " #\n #\n"
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            r.display()
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_str_representation(self):
        r = Rectangle(5, 10, 2, 3, 1)
        expected_str = "[Rectangle] (1) 2/3 - 5/10"
        self.assertEqual(str(r), expected_str)

if __name__ == '__main__':
    unittest.main()