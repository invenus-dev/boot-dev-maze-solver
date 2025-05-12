from point import Point
from tkinter import Canvas


class Line:
    def __init__(self, start: Point, end: Point):
        self.start = start
        self.end = end

    def draw(self, canvas: Canvas, color):
        canvas.create_line(
            self.start.x, self.start.y, self.end.x, self.end.y, fill=color
        )
