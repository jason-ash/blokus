"""Test point.py"""
import unittest

from blokus.point import Point


class TestPoint(unittest.TestCase):
    """Test Point class"""

    def test_corners(self):
        """Test a point's corners"""
        point = Point(4, 4)
        corners = {Point(5, 5), Point(3, 5), Point(3, 3), Point(5, 3)}
        self.assertEqual(point.corners(), corners)

    def test_sides(self):
        """Test a point's sides"""
        point = Point(4, 4)
        sides = {Point(5, 4), Point(4, 5), Point(3, 4), Point(4, 3)}
        self.assertEqual(point.sides(), sides)

    def test_is_corner(self):
        """Test identifying whether two points are corners of each other"""
        first, second, third = Point(4, 4), Point(5, 5), Point(4, 5)
        self.assertTrue(first.is_corner(second))
        self.assertTrue(second.is_corner(first))
        self.assertFalse(first.is_corner(third))
        self.assertFalse(third.is_corner(first))

    def test_is_side(self):
        """Test identifying whether two points are sides of each other"""
        first, second, third = Point(4, 4), Point(5, 5), Point(4, 5)
        self.assertTrue(first.is_side(third))
        self.assertTrue(third.is_side(second))
        self.assertFalse(first.is_side(second))
        self.assertFalse(second.is_side(first))

    def test_reflect_x(self):
        """Test reflecting a point over a vertical line"""
        point = Point(4, 4)
        x_value = 7
        reflection = Point(10, 4)
        self.assertEqual(point.reflect(x=x_value), reflection)

    def test_reflect_y(self):
        """Test reflecting a point over a horizontal line"""
        point = Point(4, 4)
        y_value = 1
        reflection = Point(4, -2)
        self.assertEqual(point.reflect(y=y_value), reflection)

    def test_reflect_xy(self):
        """Test reflecting a point over a horizontal and vertical lines"""
        point = Point(4, 4)
        x_value, y_value = 7, 1
        reflection = Point(10, -2)
        self.assertEqual(point.reflect(x=x_value, y=y_value), reflection)

    def test_reflect_identity(self):
        """Test reflecting a point over itself"""
        point = Point(4, 4)
        x_value, y_value = 4, 4
        reflection = Point(4, 4)
        self.assertEqual(point.reflect(x=x_value, y=y_value), reflection)

    def test_rotate_identity(self):
        """Test rotating a point over itself"""
        point = Point(4, 4)
        around = Point(4, 4)
        rotation = Point(4, 4)
        self.assertEqual(point.rotate(around=around, degrees=0), rotation)
        self.assertEqual(point.rotate(around=around, degrees=90), rotation)
        self.assertEqual(point.rotate(around=around, degrees=180), rotation)
        self.assertEqual(point.rotate(around=around, degrees=270), rotation)

    def test_rotate_raises(self):
        """Test raising an error for rotation degrees not multiples of 90"""
        point = Point(4, 4)
        around = Point(5, 5)
        self.assertRaises(ValueError, point.rotate, around, 120)

    def test_rotate(self):
        """Test some sample rotations"""
        point = Point(8, 10)
        around = Point(7, 7)
        self.assertEqual(point.rotate(around=around, degrees=90), Point(10, 6))
        self.assertEqual(point.rotate(around=around, degrees=180), Point(6, 4))
        self.assertEqual(point.rotate(around=around, degrees=270), Point(4, 8))
        self.assertEqual(point.rotate(around=around, degrees=-90), Point(4, 8))
