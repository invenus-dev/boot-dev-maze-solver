from line import Line
from point import Point
from window import Window
class Cell:
    visited = False

    def __init__(self, win: Window = None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.__x1 = -1
        self.__x2 = -1
        self.__y1 = -1
        self.__y2 = -1
        self.__win = win

    def draw(self, x1, y1, x2, y2):
        self.__x1 = x1
        self.__x2 = x2
        self.__y1 = y1
        self.__y2 = y2
        
        line = Line(Point(x1, y1), Point(x1, y2))
        self.__win.draw_line(line, color="black" if self.has_left_wall else "white") if self.__win else None
        line = Line(Point(x1, y1), Point(x2, y1))
        self.__win.draw_line(line, color="black" if self.has_top_wall else "white") if self.__win else None
        line = Line(Point(x2, y1), Point(x2, y2))
        self.__win.draw_line(line, color="black" if self.has_right_wall else "white") if self.__win else None
        line = Line(Point(x1, y2), Point(x2, y2))
        self.__win.draw_line(line, color="black" if self.has_bottom_wall else "white") if self.__win else None

    def draw_move(self, to_cell, undo=False):
        half_length = abs(self.__x2 - self.__x1) // 2
        x_center = half_length + self.__x1
        y_center = half_length + self.__y1

        half_length2 = abs(to_cell.__x2 - to_cell.__x1) // 2
        x_center2 = half_length2 + to_cell.__x1
        y_center2 = half_length2 + to_cell.__y1

        fill_color = "red"
        if undo:
            fill_color = "lightgray"

        line = Line(Point(x_center, y_center), Point(x_center2, y_center2))
        self.__win.draw_line(line, fill_color) if self.__win else None
