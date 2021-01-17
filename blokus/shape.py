"""Functions and classes for Board pieces (shapes)"""
from typing import FrozenSet, NamedTuple, Optional

from blokus.point import Point


class Shape(NamedTuple):  # pylint: disable=too-many-public-methods
    """Container for the points that make up a board piece (shape)"""

    origin: Point
    points: FrozenSet[Point]

    def arrangements(
        self, lower: Optional[int] = None, upper: Optional[int] = None
    ) -> FrozenSet["Shape"]:
        """
        Return all possible arrangements (rotation/reflection) of a shape.

        Optionally specify a lower and upper bound which will restrict the
        arrangements falling outside those bounds.
        """

    def corners(self) -> FrozenSet["Point"]:
        """Return a frozenset of the corners of this Shape."""
        corner_points = (p.corners() for p in self.points)
        return frozenset.union(*corner_points) - self.sides() - self.points

    def sides(self) -> FrozenSet["Point"]:
        """Return a frozenset of the sides of this Shape."""
        side_points = (p.sides() for p in self.points)
        return frozenset.union(*side_points) - self.points

    def size(self) -> int:
        """Return the size of this shape (the number of points.)"""
        return len(self.points)

    # pylint: disable=invalid-name
    def reflect(self, x: Optional[int] = None, y: Optional[int] = None) -> "Shape":
        """Return a new shape by reflecting over x and/or y lines."""
        origin = self.origin.reflect(x, y)
        reflected = (point.reflect(x, y) for point in self.points)
        return Shape(origin=origin, points=frozenset(reflected))

    def rotate(self, around: Point, degrees: int) -> "Shape":
        """Return a new shape rotated by n degrees around a Point."""
        origin = self.origin.rotate(around, degrees)
        rotated = (point.rotate(around, degrees) for point in self.points)
        return Shape(origin=origin, points=frozenset(rotated))

    @classmethod
    def I1(cls, origin: Point) -> "Shape":  # pylint: disable=invalid-name
        """
        Return the I1 shape.

        [X]
        """
        return Shape(origin=origin, points=frozenset([origin]))

    @classmethod
    def I2(cls, origin: Point) -> "Shape":  # pylint: disable=invalid-name
        """
        Return the I2 shape.

        [X][ ]
        """
        points = [origin, Point(x=origin.x + 1, y=origin.y)]
        return Shape(origin=origin, points=frozenset(points))

    @classmethod
    def I3(cls, origin: Point) -> "Shape":  # pylint: disable=invalid-name
        """
        Return the I3 shape.

        [X][ ][ ]
        """
        points = [
            origin,
            Point(x=origin.x + 1, y=origin.y),
            Point(x=origin.x + 2, y=origin.y),
        ]
        return Shape(origin=origin, points=frozenset(points))

    @classmethod
    def V3(cls, origin: Point) -> "Shape":  # pylint: disable=invalid-name
        """
        Return the V3 shape.

        [ ]
        [X][ ]
        """
        points = [
            origin,
            Point(x=origin.x, y=origin.y + 1),
            Point(x=origin.x + 1, y=origin.y),
        ]
        return Shape(origin=origin, points=frozenset(points))

    @classmethod
    def I4(cls, origin: Point) -> "Shape":  # pylint: disable=invalid-name
        """
        Return the I4 shape.

        [X][ ][ ][ ]
        """
        points = [
            origin,
            Point(x=origin.x + 1, y=origin.y),
            Point(x=origin.x + 2, y=origin.y),
            Point(x=origin.x + 3, y=origin.y),
        ]
        return Shape(origin=origin, points=frozenset(points))

    @classmethod
    def L4(cls, origin: Point) -> "Shape":  # pylint: disable=invalid-name
        """
        Return the L4 shape.

        [ ]
        [X][ ][ ]
        """
        points = [
            origin,
            Point(x=origin.x, y=origin.y + 1),
            Point(x=origin.x + 1, y=origin.y),
            Point(x=origin.x + 2, y=origin.y),
        ]
        return Shape(origin=origin, points=frozenset(points))

    @classmethod
    def O4(cls, origin: Point) -> "Shape":  # pylint: disable=invalid-name
        """
        Return the O4 shape.

        [ ][ ]
        [X][ ]
        """
        points = [
            origin,
            Point(x=origin.x, y=origin.y + 1),
            Point(x=origin.x + 1, y=origin.y),
            Point(x=origin.x + 1, y=origin.y + 1),
        ]
        return Shape(origin=origin, points=frozenset(points))

    @classmethod
    def T4(cls, origin: Point) -> "Shape":  # pylint: disable=invalid-name
        """
        Return the T4 shape.

           [ ]
        [ ][X][ ]
        """
        points = [
            origin,
            Point(x=origin.x - 1, y=origin.y),
            Point(x=origin.x + 1, y=origin.y),
            Point(x=origin.x, y=origin.y + 1),
        ]
        return Shape(origin=origin, points=frozenset(points))

    @classmethod
    def Z4(cls, origin: Point) -> "Shape":  # pylint: disable=invalid-name
        """
        Return the Z4 shape.

           [ ][ ]
        [X][ ]
        """
        points = [
            origin,
            Point(x=origin.x + 1, y=origin.y),
            Point(x=origin.x + 1, y=origin.y + 1),
            Point(x=origin.x + 2, y=origin.y + 1),
        ]
        return Shape(origin=origin, points=frozenset(points))

    @classmethod
    def F(cls, origin: Point) -> "Shape":  # pylint: disable=invalid-name
        """
        Return the F shape.

           [ ]
           [X][ ]
        [ ][ ]
        """
        points = [
            origin,
            Point(x=origin.x + 1, y=origin.y),
            Point(x=origin.x + 1, y=origin.y + 1),
            Point(x=origin.x + 2, y=origin.y + 1),
            Point(x=origin.x + 1, y=origin.y + 2),
        ]
        return Shape(origin=origin, points=frozenset(points))

    @classmethod
    def I5(cls, origin: Point) -> "Shape":  # pylint: disable=invalid-name
        """
        Return the I5 shape.

        [X][ ][ ][ ][ ]
        """
        points = [
            origin,
            Point(x=origin.x + 1, y=origin.y),
            Point(x=origin.x + 2, y=origin.y),
            Point(x=origin.x + 3, y=origin.y),
            Point(x=origin.x + 4, y=origin.y),
        ]
        return Shape(origin=origin, points=frozenset(points))

    @classmethod
    def L5(cls, origin: Point) -> "Shape":  # pylint: disable=invalid-name
        """
        Return the L5 shape.

        [ ]
        [X][ ][ ][ ]
        """
        points = [
            origin,
            Point(x=origin.x, y=origin.y + 1),
            Point(x=origin.x + 1, y=origin.y),
            Point(x=origin.x + 2, y=origin.y),
            Point(x=origin.x + 3, y=origin.y),
        ]
        return Shape(origin=origin, points=frozenset(points))

    @classmethod
    def N(cls, origin: Point) -> "Shape":  # pylint: disable=invalid-name
        """
        Return the N shape.

              [ ][ ]
        [X][ ][ ]
        """
        points = [
            origin,
            Point(x=origin.x + 1, y=origin.y),
            Point(x=origin.x + 2, y=origin.y),
            Point(x=origin.x + 2, y=origin.y + 1),
            Point(x=origin.x + 3, y=origin.y + 1),
        ]
        return Shape(origin=origin, points=frozenset(points))

    @classmethod
    def P(cls, origin: Point) -> "Shape":  # pylint: disable=invalid-name
        """
        Return the P shape.

           [ ][ ]
        [X][ ][ ]
        """
        points = [
            origin,
            Point(x=origin.x + 1, y=origin.y),
            Point(x=origin.x + 1, y=origin.y + 1),
            Point(x=origin.x + 2, y=origin.y),
            Point(x=origin.x + 2, y=origin.y + 1),
        ]
        return Shape(origin=origin, points=frozenset(points))

    @classmethod
    def U(cls, origin: Point) -> "Shape":  # pylint: disable=invalid-name
        """
        Return the U shape.

        [ ]   [ ]
        [ ][X][ ]
        """
        points = [
            origin,
            Point(x=origin.x - 1, y=origin.y),
            Point(x=origin.x - 1, y=origin.y + 1),
            Point(x=origin.x + 1, y=origin.y),
            Point(x=origin.x + 1, y=origin.y + 1),
        ]
        return Shape(origin=origin, points=frozenset(points))

    @classmethod
    def V5(cls, origin: Point) -> "Shape":  # pylint: disable=invalid-name
        """
        Return the V5 shape.

        [ ]
        [ ]
        [X][ ][ ]
        """
        points = [
            origin,
            Point(x=origin.x, y=origin.y + 1),
            Point(x=origin.x, y=origin.y + 2),
            Point(x=origin.x + 1, y=origin.y),
            Point(x=origin.x + 2, y=origin.y),
        ]
        return Shape(origin=origin, points=frozenset(points))

    @classmethod
    def W(cls, origin: Point) -> "Shape":  # pylint: disable=invalid-name
        """
        Return the W shape.

              [ ]
           [X][ ]
        [ ][ ]
        """
        points = [
            origin,
            Point(x=origin.x - 1, y=origin.y - 1),
            Point(x=origin.x, y=origin.y - 1),
            Point(x=origin.x + 1, y=origin.y),
            Point(x=origin.x + 1, y=origin.y + 1),
        ]
        return Shape(origin=origin, points=frozenset(points))

    @classmethod
    def X(cls, origin: Point) -> "Shape":  # pylint: disable=invalid-name
        """
        Return the X shape.

           [ ]
        [ ][X][ ]
           [ ]
        """
        points = [
            origin,
            Point(x=origin.x - 1, y=origin.y),
            Point(x=origin.x + 1, y=origin.y),
            Point(x=origin.x, y=origin.y - 1),
            Point(x=origin.x, y=origin.y + 1),
        ]
        return Shape(origin=origin, points=frozenset(points))

    @classmethod
    def Y(cls, origin: Point) -> "Shape":  # pylint: disable=invalid-name
        """
        Return the Y shape.

           [ ]
        [ ][X][ ][ ]
        """
        points = [
            origin,
            Point(x=origin.x - 1, y=origin.y),
            Point(x=origin.x, y=origin.y + 1),
            Point(x=origin.x + 1, y=origin.y),
            Point(x=origin.x + 2, y=origin.y),
        ]
        return Shape(origin=origin, points=frozenset(points))

    @classmethod
    def Z5(cls, origin: Point) -> "Shape":  # pylint: disable=invalid-name
        """
        Return the Z5 shape.

           [ ][ ]
           [X]
        [ ][ ]
        """
        points = [
            origin,
            Point(x=origin.x - 1, y=origin.y - 1),
            Point(x=origin.x, y=origin.y - 1),
            Point(x=origin.x, y=origin.y + 1),
            Point(x=origin.x + 1, y=origin.y + 1),
        ]
        return Shape(origin=origin, points=frozenset(points))
