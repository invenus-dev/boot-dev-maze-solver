from window import Window
from line import Line
from point import Point


def main():
    win = Window(800, 600)

    win.draw_line(Line(Point(100, 100), Point(200, 200)), "red")
    win.draw_line(Line(Point(100, 400), Point(500, 400)), "black")

    win.wait_for_close()


main()
