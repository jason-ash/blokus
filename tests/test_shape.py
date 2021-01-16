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

    def test_simple_reflection(self):
        """Test reflecting a shape containing a single point"""
        origin = Point(4, 4)
        x_value, y_value = 7, 6
        shape = Shape.I1(origin)
        self.assertEqual(shape.reflect(x=x_value).origin, origin.reflect(x=x_value))
        self.assertEqual(shape.reflect(y=y_value).origin, origin.reflect(y=y_value))
        self.assertEqual(
            shape.reflect(x=x_value, y=y_value).origin,
            origin.reflect(x=x_value, y=y_value),
        )

    def test_simple_rotation(self):
        """Test rotating a shape containing a single point"""
        origin = Point(4, 4)
        around = Point(7, 6)
        shape = Shape.I1(origin)
        self.assertEqual(shape.rotate(around, 90).origin, origin.rotate(around, 90))
        self.assertEqual(shape.rotate(around, 180).origin, origin.rotate(around, 180))
        self.assertEqual(shape.rotate(around, 270).origin, origin.rotate(around, 270))
