"""Test point.py"""
import unittest

from blokus.point import Point


class TestPoint(unittest.TestCase):
    """Test Point class"""

    def test_corners(self):
        """Test a point's corners"""
        point = Point(4, 4)
        corners = [Point(5, 5), Point(3, 5), Point(3, 3), Point(5, 3)]
        self.assertEqual(point.corners(), frozenset(corners))

    def test_sides(self):
        """Test a point's sides"""
        point = Point(4, 4)
        sides = [Point(5, 4), Point(4, 5), Point(3, 4), Point(4, 3)]
        self.assertEqual(point.sides(), frozenset(sides))

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
