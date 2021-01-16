"""Test shape.py"""
import unittest

from blokus.point import Point
from blokus.shape import Shape


class TestShape(unittest.TestCase):
    """Test Shape class"""

    def test_simple_sides(self):
        """Test returning the sides of a shape containing a single point"""
        origin = Point(4, 4)
        shape = Shape.I1(origin)
        self.assertEqual(shape.sides(), origin.sides())

    def test_simple_corners(self):
        """Test returning the corners of a shape containing a single point"""
        origin = Point(4, 4)
        shape = Shape.I1(origin)
        self.assertEqual(shape.corners(), origin.corners())
