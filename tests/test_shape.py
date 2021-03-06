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

    def test_w_sides(self):
        """Test returning the sides of the W shape"""
        shape = Shape.W(Point(5, 5))
        sides = {
            Point(3, 4),
            Point(4, 3),
            Point(4, 5),
            Point(5, 3),
            Point(5, 6),
            Point(6, 4),
            Point(6, 7),
            Point(7, 5),
            Point(7, 6),
        }
        self.assertEqual(shape.sides(), sides)

    def test_w_corners(self):
        """Test returning the corners of the W shape"""
        shape = Shape.W(Point(5, 5))
        corners = {
            Point(3, 3),
            Point(3, 5),
            Point(4, 6),
            Point(5, 7),
            Point(6, 3),
            Point(7, 4),
            Point(7, 7),
        }
        self.assertEqual(shape.corners(), corners)

    def test_w_rotation(self):
        """Test rotating the W shape"""
        origin = Point(5, 5)
        shape = Shape.W(origin)
        shape = shape.rotate(around=shape.origin, degrees=180)
        points = {Point(5, 5), Point(6, 6), Point(4, 4), Point(4, 5), Point(5, 6)}
        self.assertEqual(shape.points, points)
        self.assertEqual(shape.origin, origin)

    def test_w_reflection(self):
        """Test reflecting the W shape"""
        origin = Point(5, 5)
        shape = Shape.W(origin)
        shape = shape.reflect(x=8)
        points = {Point(12, 4), Point(11, 4), Point(11, 5), Point(10, 5), Point(10, 6)}
        self.assertEqual(shape.points, points)
        self.assertEqual(shape.origin, Point(11, 5))

    def test_complex_shape_corners(self):
        """Test identifying the corners of a complex shape"""
        #    [X]   [X]
        # [X]   [ ]   [X]
        #    [ ][ ][ ]         [X]
        #    [ ]      [ ][ ][ ]
        # [X]   [ ][ ]   [ ][ ]   [X]
        #    [X]   [ ][ ]      [ ]
        #       [ ]   [ ]   [ ][ ]
        # [ ][ ][ ]         [ ]   [X]
        # [ ]      [X]   [X]   [X]
        origin = Point(0, 0)
        # fmt: off
        points = {
            Point(0, 0), Point(0, 1), Point(1, 1), Point(2, 1), Point(2, 2),  # Z
            Point(3, 3), Point(2, 4), Point(3, 4), Point(4, 3), Point(4, 2),  # W
            Point(4, 5), Point(5, 5), Point(6, 5), Point(5, 4), Point(6, 4),  # P
            Point(1, 5), Point(1, 6), Point(2, 6), Point(2, 7), Point(3, 6),  # F
            Point(7, 3), Point(7, 2), Point(6, 2), Point(6, 1),  # Z4
        }
        corners = {
            Point(3, 0), Point(5, 0), Point(7, 0), Point(8, 1),
            Point(8, 4), Point(7, 6), Point(4, 7), Point(3, 8),
            Point(1, 8), Point(0, 7), Point(0, 4), Point(1, 3),
            Point(-1, 2), Point(-1, -1), Point(1, -1),  # trivial points outside board
        }
        # fmt: on
        shape = Shape(origin=origin, points=points)
        self.assertEqual(shape.corners(), corners)

    def test_can_connect_true(self):
        """Test two shapes that are allowed to connect"""
        first = Shape.V3(Point(5, 5))
        second = Shape.V3(Point(4, 4)).rotate(Point(4, 4), degrees=180)
        self.assertTrue(first.can_connect(second))

    def test_can_connect_false(self):
        """Test two shapes that are not allowed to connect"""
        first = Shape.V3(Point(5, 5))
        second = Shape.V3(Point(5, 4)).rotate(Point(5, 4), degrees=180)
        self.assertFalse(first.can_connect(second))
