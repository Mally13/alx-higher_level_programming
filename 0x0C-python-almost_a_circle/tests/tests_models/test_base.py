#!/usr/bin/python3
# test_base.py
"""Defines unittests for base.py"""
import os
import unittest
from models.base import Base


class TestBase_Instantiation(unittest.TestCase):

    def test_init_with_id(self):
        """With arguments"""
        obj = Base(10)
        self.assertEqual(obj.id, 10)

    def test_init_without_id(self):
        """Without aguments"""
        obj1 = Base()
        obj2 = Base()
        self.assertEqual(obj1.id, 1)
        self.assertEqual(obj2.id, 2)

    def test_private_attribute(self):
        """Check for private attributes"""
        obj = Base()
        with self.assertRaises(AttributeError):
            print(obj.__nb_objects)

if __name__ == '__main__':
    unittest.main()

