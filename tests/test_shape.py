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

    def test_complex_sides(self):
        """Test returning the sides of a complex shape"""
        shape = Shape.W(Point(4, 4))
        sides = [
            Point(3, 4),
            Point(4, 3),
            Point(4, 5),
            Point(5, 3),
            Point(5, 6),
            Point(6, 4),
            Point(6, 7),
            Point(7, 5),
            Point(7, 6),
        ]
        self.assertEqual(shape.sides(), frozenset(sides))

    def test_complex_corners(self):
        """Test returning the corners of a complex shape"""
        shape = Shape.W(Point(4, 4))
        corners = [
            Point(3, 3),
            Point(3, 5),
            Point(4, 6),
            Point(5, 7),
            Point(6, 3),
            Point(7, 4),
            Point(7, 7),
        ]
        self.assertEqual(shape.corners(), frozenset(corners))

    def test_complex_rotation(self):
        """Test rotating a complex shape"""
        origin = Point(4, 4)
        shape = Shape.W(origin)
        shape = shape.rotate(around=shape.origin, degrees=180)
        points = [
            Point(4, 4),
            Point(3, 4),
            Point(3, 3),
            Point(2, 3),
            Point(2, 2),
        ]
        self.assertEqual(shape.points, frozenset(points))
        self.assertEqual(shape.origin, origin)

    def test_complex_reflection(self):
        """Test reflecting a complex shape"""
        origin = Point(4, 4)
        shape = Shape.W(origin)
        shape = shape.reflect(x=8)
        points = [
            Point(12, 4),
            Point(11, 4),
            Point(11, 5),
            Point(10, 5),
            Point(10, 6),
        ]
        self.assertEqual(shape.points, frozenset(points))
        self.assertEqual(shape.origin, Point(12, 4))
