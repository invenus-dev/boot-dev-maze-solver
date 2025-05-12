from line import Line
from point import Point
from window import Window


class Cell:
    def __init__(self, topLeft: Point, bottomRight: Point, win: Window):
        self._x1 = topLeft.x
        self._y1 = topLeft.y
        self._x2 = bottomRight.x
        self._y2 = bottomRight.y
        self._win = win
        self.has_left_wall = True
        self.has_top_wall = True
        self.has_right_wall = True
        self.has_bottom_wall = True

    def draw(self):
        # Draw walls of the cell
        if self.has_left_wall:
            self._win.draw_line(
                Line(Point(self._x1, self._y1), Point(self._x1, self._y2)), "black"
            )
        if self.has_top_wall:
            self._win.draw_line(
                Line(Point(self._x1, self._y1), Point(self._x2, self._y1)), "black"
            )
        if self.has_right_wall:
            self._win.draw_line(
                Line(Point(self._x2, self._y1), Point(self._x2, self._y2)), "black"
            )
        if self.has_bottom_wall:
            self._win.draw_line(
                Line(Point(self._x1, self._y2), Point(self._x2, self._y2)), "black"
            )
