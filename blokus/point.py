"""Functions and classes related to Points on the board"""
from typing import FrozenSet, NamedTuple, Optional


class Point(NamedTuple):
    """Container representing x and y coordinates for a single Point"""

    x: int
    y: int

    def corners(self) -> FrozenSet["Point"]:
        """Return a frozenset of corners of a Point."""
        points = [
            Point(x=self.x + 1, y=self.y + 1),
            Point(x=self.x - 1, y=self.y + 1),
            Point(x=self.x - 1, y=self.y - 1),
            Point(x=self.x + 1, y=self.y - 1),
        ]
        return frozenset(points)

    def sides(self) -> FrozenSet["Point"]:
        """Return a frozenset of the sides of a Point."""
        points = [
            Point(x=self.x + 1, y=self.y),
            Point(x=self.x, y=self.y + 1),
            Point(x=self.x - 1, y=self.y),
            Point(x=self.x, y=self.y - 1),
        ]
        return frozenset(points)

    def is_corner(self, other: "Point") -> bool:
        """Return a boolean indicating whether two points are corners of each other."""
        return other in self.corners()

    def is_side(self, other: "Point") -> bool:
        """Return a boolean indicating whether two points are sides of each other."""
        return other in self.sides()

    # pylint: disable=invalid-name
    def reflect(self, x: Optional[int] = None, y: Optional[int] = None) -> "Point":
        """
        Return a new Point by reflecting across x and/or y values.

        Examples
        --------
        >>> Point(4, 5).reflect()
        Point(x=4, y=5)
        >>> Point(4, 5).reflect(x=5)
        Point(x=6, y=5)
        >>> Point(4, 5).reflect(y=2)
        Point(x=4, y=-1)
        >>> Point(4, 5).reflect(x=6, y=6)
        Point(x=8, y=7)
        """
        x = x or self.x
        y = y or self.y
        dx = x - self.x
        dy = y - self.y
        return Point(x=x + dx, y=y + dy)

    # pylint: disable=invalid-name
    def rotate(self, around: "Point", degrees: int) -> "Point":
        """
        Return a new Point by rotating n degrees around another Point.

        Parameters
        ----------
        around : Point, the point around which to rotate
        degrees : int, the number of degrees to rotate in multiples of 90.

        Examples
        --------
        >>> Point(8, 10).rotate(around=Point(7, 7), degrees=90)
        Point(x=10, y=6)
        >>> Point(8, 10).rotate(around=Point(7, 7), degrees=180)
        Point(x=6, y=4)
        >>> Point(8, 10).rotate(around=Point(7, 7), degrees=270)
        Point(x=4, y=8)
        >>> Point(8, 10).rotate(around=Point(7, 7), degrees=360)
        Point(x=8, y=10)
        >>> Point(8, 10).rotate(around=Point(7, 7), degrees=-90)
        Point(x=4, y=8)
        >>> Point(5, 5).rotate(around=Point(5, 5), degrees=180)
        Point(x=5, y=5)
        >>> Point(8, 10).rotate(around=Point(x=7, y=7), degrees=120)
        Traceback (most recent call last):
        ...
        ValueError: degrees must be a multiple of 90
        """
        # constrain degrees to 0, 90, 180, 270; otherwise raise an error
        degrees = degrees % 360
        if degrees not in [0, 90, 180, 270]:
            raise ValueError("degrees must be a multiple of 90")

        if degrees == 0:
            return Point(x=self.x, y=self.y)

        # recursively rotate 90 degrees at a time until we reach our goal
        dx, dy = self.x - around.x, self.y - around.y
        x, y = around.x + dy, around.y - dx
        return Point(x=x, y=y).rotate(around=around, degrees=degrees - 90)
