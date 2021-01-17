"""Functions and classes for Board pieces (shapes)"""
from typing import NamedTuple, Optional, Set

from blokus.point import Point


class Shape(NamedTuple):  # pylint: disable=too-many-public-methods
    """Container for the points that make up a board piece (shape)"""

    origin: Point
    points: Set[Point]

    def is_within(
        self, lower: Optional[int] = None, upper: Optional[int] = None
    ) -> bool:
        """
        Return a boolean indicating if a shape is contained within a boundary.

        If any of the shape's points fall outside the boundary, then return False.
        """
        if lower is None:
            lower = min(min(p.x, p.y) for p in self.points)
        if upper is None:
            upper = max(max(p.x, p.y) for p in self.points)
        return all(
            (lower <= p.x <= upper) and (lower <= p.y <= upper) for p in self.points
        )

    def arrangements(
        self, lower: Optional[int] = None, upper: Optional[int] = None
    ) -> Set["Shape"]:
        """
        Return all possible arrangements (rotation/reflection) of a shape.

        Optionally specify a lower and upper bound (inclusive) for the x and y axes,
        which removes any arrangements that fall outside those bounds. (For example,
        those that result in negative x or y values.)
        """
        # we can create up to 8 different shapes by reflecting across one axis and
        # rotating 90, 180, and 270 degrees. Then we return a frozenset of all unique
        # shapes that are created by the different transformations.
        transformations = [
            self.rotate(around=self.origin, degrees=0),
            self.rotate(around=self.origin, degrees=90),
            self.rotate(around=self.origin, degrees=180),
            self.rotate(around=self.origin, degrees=270),
        ]
        reflection = self.reflect(x=self.origin.x)
        transformations += [
            reflection.rotate(around=reflection.origin, degrees=0),
            reflection.rotate(around=reflection.origin, degrees=90),
            reflection.rotate(around=reflection.origin, degrees=180),
            reflection.rotate(around=reflection.origin, degrees=270),
        ]

        # remove any transformations that fall outside the lower/upper boundaries
        valid = (t for t in transformations if t.is_within(lower=lower, upper=upper))
        return frozenset(valid)

    def can_connect(self, other: "Shape") -> bool:
        """
        Return a boolean indicating whether or not two shapes can connect.

        According to the rules of the game, two shapes can connect if they meet at a
        corner, e.g. like the following diagram shows. We must check two conditions:
            1. If any of the first shape's corners are points in the second shape.
            2. If any of the first shape's sides are points in the second shape.
        Both conditions are reciprocal, so we can test only one direction each.

        X can connect to Y        X cannot connect to Y
        ------------------        ---------------------
              [Y]                    [Y]
              [Y][Y]                 [Y][Y]
        [X][X]                    [X][X]
           [X]                       [X]
        """
        # do any of this shape's corners intersect with the other shape's points?
        # if not, we can return False right away; otherwise we will continue.
        if self.corners().isdisjoint(other.points):
            return False

        # now we know the shapes share at least one corner connection. We must test
        # whether the sides of the shapes are touching, and return this result.
        return self.sides().isdisjoint(other.points)

    def corners(self) -> Set["Point"]:
        """Return a set of the corners of this Shape."""
        all_corners = set.union(*(p.corners() for p in self.points))
        return all_corners - self.sides() - self.points

    def sides(self) -> Set["Point"]:
        """Return a set of the sides of this Shape."""
        all_sides = set.union(*(p.sides() for p in self.points))
        return all_sides - self.points

    def size(self) -> int:
        """Return the size of this shape (the number of points.)"""
        return len(self.points)

    # pylint: disable=invalid-name
    def reflect(self, x: Optional[int] = None, y: Optional[int] = None) -> "Shape":
        """Return a new shape by reflecting over x and/or y lines."""
        origin = self.origin.reflect(x, y)
        reflected = {point.reflect(x, y) for point in self.points}
        return Shape(origin=origin, points=reflected)

    def rotate(self, around: Point, degrees: int) -> "Shape":
        """Return a new shape rotated by n degrees around a Point."""
        origin = self.origin.rotate(around, degrees)
        rotated = {point.rotate(around, degrees) for point in self.points}
        return Shape(origin=origin, points=rotated)

    @classmethod
    def I1(cls, origin: Point) -> "Shape":  # pylint: disable=invalid-name
        """
        Return the I1 shape.

        [X]
        """
        return Shape(origin=origin, points={origin})

    @classmethod
    def I2(cls, origin: Point) -> "Shape":  # pylint: disable=invalid-name
        """
        Return the I2 shape.

        [X][ ]
        """
        points = {origin, Point(x=origin.x + 1, y=origin.y)}
        return Shape(origin=origin, points=points)

    @classmethod
    def I3(cls, origin: Point) -> "Shape":  # pylint: disable=invalid-name
        """
        Return the I3 shape.

        [X][ ][ ]
        """
        points = {
            origin,
            Point(x=origin.x + 1, y=origin.y),
            Point(x=origin.x + 2, y=origin.y),
        }
        return Shape(origin=origin, points=points)

    @classmethod
    def V3(cls, origin: Point) -> "Shape":  # pylint: disable=invalid-name
        """
        Return the V3 shape.

        [ ]
        [X][ ]
        """
        points = {
            origin,
            Point(x=origin.x, y=origin.y + 1),
            Point(x=origin.x + 1, y=origin.y),
        }
        return Shape(origin=origin, points=points)

    @classmethod
    def I4(cls, origin: Point) -> "Shape":  # pylint: disable=invalid-name
        """
        Return the I4 shape.

        [X][ ][ ][ ]
        """
        points = {
            origin,
            Point(x=origin.x + 1, y=origin.y),
            Point(x=origin.x + 2, y=origin.y),
            Point(x=origin.x + 3, y=origin.y),
        }
        return Shape(origin=origin, points=points)

    @classmethod
    def L4(cls, origin: Point) -> "Shape":  # pylint: disable=invalid-name
        """
        Return the L4 shape.

        [ ]
        [X][ ][ ]
        """
        points = {
            origin,
            Point(x=origin.x, y=origin.y + 1),
            Point(x=origin.x + 1, y=origin.y),
            Point(x=origin.x + 2, y=origin.y),
        }
        return Shape(origin=origin, points=points)

    @classmethod
    def O4(cls, origin: Point) -> "Shape":  # pylint: disable=invalid-name
        """
        Return the O4 shape.

        [ ][ ]
        [X][ ]
        """
        points = {
            origin,
            Point(x=origin.x, y=origin.y + 1),
            Point(x=origin.x + 1, y=origin.y),
            Point(x=origin.x + 1, y=origin.y + 1),
        }
        return Shape(origin=origin, points=points)

    @classmethod
    def T4(cls, origin: Point) -> "Shape":  # pylint: disable=invalid-name
        """
        Return the T4 shape.

           [ ]
        [ ][X][ ]
        """
        points = {
            origin,
            Point(x=origin.x - 1, y=origin.y),
            Point(x=origin.x + 1, y=origin.y),
            Point(x=origin.x, y=origin.y + 1),
        }
        return Shape(origin=origin, points=points)

    @classmethod
    def Z4(cls, origin: Point) -> "Shape":  # pylint: disable=invalid-name
        """
        Return the Z4 shape.

           [ ][ ]
        [X][ ]
        """
        points = {
            origin,
            Point(x=origin.x + 1, y=origin.y),
            Point(x=origin.x + 1, y=origin.y + 1),
            Point(x=origin.x + 2, y=origin.y + 1),
        }
        return Shape(origin=origin, points=points)

    @classmethod
    def F(cls, origin: Point) -> "Shape":  # pylint: disable=invalid-name
        """
        Return the F shape.

           [ ]
           [X][ ]
        [ ][ ]
        """
        points = {
            origin,
            Point(x=origin.x + 1, y=origin.y),
            Point(x=origin.x + 1, y=origin.y + 1),
            Point(x=origin.x + 2, y=origin.y + 1),
            Point(x=origin.x + 1, y=origin.y + 2),
        }
        return Shape(origin=origin, points=points)

    @classmethod
    def I5(cls, origin: Point) -> "Shape":  # pylint: disable=invalid-name
        """
        Return the I5 shape.

        [X][ ][ ][ ][ ]
        """
        points = {
            origin,
            Point(x=origin.x + 1, y=origin.y),
            Point(x=origin.x + 2, y=origin.y),
            Point(x=origin.x + 3, y=origin.y),
            Point(x=origin.x + 4, y=origin.y),
        }
        return Shape(origin=origin, points=points)

    @classmethod
    def L5(cls, origin: Point) -> "Shape":  # pylint: disable=invalid-name
        """
        Return the L5 shape.

        [ ]
        [X][ ][ ][ ]
        """
        points = {
            origin,
            Point(x=origin.x, y=origin.y + 1),
            Point(x=origin.x + 1, y=origin.y),
            Point(x=origin.x + 2, y=origin.y),
            Point(x=origin.x + 3, y=origin.y),
        }
        return Shape(origin=origin, points=points)

    @classmethod
    def N(cls, origin: Point) -> "Shape":  # pylint: disable=invalid-name
        """
        Return the N shape.

              [ ][ ]
        [X][ ][ ]
        """
        points = {
            origin,
            Point(x=origin.x + 1, y=origin.y),
            Point(x=origin.x + 2, y=origin.y),
            Point(x=origin.x + 2, y=origin.y + 1),
            Point(x=origin.x + 3, y=origin.y + 1),
        }
        return Shape(origin=origin, points=points)

    @classmethod
    def P(cls, origin: Point) -> "Shape":  # pylint: disable=invalid-name
        """
        Return the P shape.

           [ ][ ]
        [X][ ][ ]
        """
        points = {
            origin,
            Point(x=origin.x + 1, y=origin.y),
            Point(x=origin.x + 1, y=origin.y + 1),
            Point(x=origin.x + 2, y=origin.y),
            Point(x=origin.x + 2, y=origin.y + 1),
        }
        return Shape(origin=origin, points=points)

    @classmethod
    def U(cls, origin: Point) -> "Shape":  # pylint: disable=invalid-name
        """
        Return the U shape.

        [ ]   [ ]
        [ ][X][ ]
        """
        points = {
            origin,
            Point(x=origin.x - 1, y=origin.y),
            Point(x=origin.x - 1, y=origin.y + 1),
            Point(x=origin.x + 1, y=origin.y),
            Point(x=origin.x + 1, y=origin.y + 1),
        }
        return Shape(origin=origin, points=points)

    @classmethod
    def V5(cls, origin: Point) -> "Shape":  # pylint: disable=invalid-name
        """
        Return the V5 shape.

        [ ]
        [ ]
        [X][ ][ ]
        """
        points = {
            origin,
            Point(x=origin.x, y=origin.y + 1),
            Point(x=origin.x, y=origin.y + 2),
            Point(x=origin.x + 1, y=origin.y),
            Point(x=origin.x + 2, y=origin.y),
        }
        return Shape(origin=origin, points=points)

    @classmethod
    def W(cls, origin: Point) -> "Shape":  # pylint: disable=invalid-name
        """
        Return the W shape.

              [ ]
           [X][ ]
        [ ][ ]
        """
        points = {
            origin,
            Point(x=origin.x - 1, y=origin.y - 1),
            Point(x=origin.x, y=origin.y - 1),
            Point(x=origin.x + 1, y=origin.y),
            Point(x=origin.x + 1, y=origin.y + 1),
        }
        return Shape(origin=origin, points=points)

    @classmethod
    def X(cls, origin: Point) -> "Shape":  # pylint: disable=invalid-name
        """
        Return the X shape.

           [ ]
        [ ][X][ ]
           [ ]
        """
        points = {
            origin,
            Point(x=origin.x - 1, y=origin.y),
            Point(x=origin.x + 1, y=origin.y),
            Point(x=origin.x, y=origin.y - 1),
            Point(x=origin.x, y=origin.y + 1),
        }
        return Shape(origin=origin, points=points)

    @classmethod
    def Y(cls, origin: Point) -> "Shape":  # pylint: disable=invalid-name
        """
        Return the Y shape.

           [ ]
        [ ][X][ ][ ]
        """
        points = {
            origin,
            Point(x=origin.x - 1, y=origin.y),
            Point(x=origin.x, y=origin.y + 1),
            Point(x=origin.x + 1, y=origin.y),
            Point(x=origin.x + 2, y=origin.y),
        }
        return Shape(origin=origin, points=points)

    @classmethod
    def Z5(cls, origin: Point) -> "Shape":  # pylint: disable=invalid-name
        """
        Return the Z5 shape.

           [ ][ ]
           [X]
        [ ][ ]
        """
        points = {
            origin,
            Point(x=origin.x - 1, y=origin.y - 1),
            Point(x=origin.x, y=origin.y - 1),
            Point(x=origin.x, y=origin.y + 1),
            Point(x=origin.x + 1, y=origin.y + 1),
        }
        return Shape(origin=origin, points=points)
