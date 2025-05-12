from tkinter import Tk, BOTH, Canvas
from line import Line

class Window:

    def __init__(self, width, height):
        self.root_widget = Tk()
        self.root_widget.title("Window")
        self.canvas = Canvas(self.root_widget, width=width, height=height)
        self.canvas.pack(fill=BOTH, expand=True)
        self.running = False
        self.root_widget.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.root_widget.update_idletasks()
        self.root_widget.update()

    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()

    def close(self):
        self.running = False
    
    def draw_line(self, line: Line, color="black"):
        line.draw(self.canvas, color)
