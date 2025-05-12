from window import Window
from point import Point
from cell import Cell


def main():
    win = Window(800, 600)

    c1 = Cell(Point(100, 100), Point(150, 150), win)
    c1.draw()
    c2 = Cell(Point(150, 150), Point(200, 200), win)
    c2.has_top_wall = False
    c2.draw()

    win.wait_for_close()


main()
