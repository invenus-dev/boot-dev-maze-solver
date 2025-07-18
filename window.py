from tkinter import Tk, BOTH, Canvas
from line import Line

class Window:

    def __init__(self, width, height, center_on_active=True):
        self.root_widget = Tk()
        self.root_widget.title("Window")
        
        # Hide initially
        self.root_widget.withdraw()
        self.root_widget.update_idletasks()
        
        if center_on_active:
            # Get mouse position to determine active screen
            mouse_x = self.root_widget.winfo_pointerx()
            mouse_y = self.root_widget.winfo_pointery()
            
            # Get screen dimensions
            screen_width = self.root_widget.winfo_screenwidth()
            screen_height = self.root_widget.winfo_screenheight()
            
            # Calculate center based on mouse position (active screen)
            x = mouse_x - width // 2
            y = mouse_y - height // 2
            
            # Ensure window stays on screen
            x = max(0, min(x, screen_width - width))
            y = max(25, min(y, screen_height - height - 80))
        else:
            x, y = 100, 100
            
        self.root_widget.geometry(f"{width}x{height}+{x}+{y}")
        
        # Force to front and active
        self.root_widget.lift()
        self.root_widget.attributes('-topmost', True)
        self.root_widget.focus_force()
        
        # Show window
        self.root_widget.deiconify()
        
        # Remove topmost after showing
        self.root_widget.after(100, lambda: self.root_widget.attributes('-topmost', False))
        
        self.canvas = Canvas(self.root_widget, width=width, height=height, bg="white")
        self.canvas.pack(fill=BOTH, expand=True)
        self.root_widget.protocol("WM_DELETE_WINDOW", self.close)


    def redraw(self):
        self.root_widget.update_idletasks()
        self.root_widget.update()

    def wait_for_close(self):
        self.root_widget.mainloop()

    def close(self):
        self.root_widget.destroy()
    
    def draw_line(self, line: Line, color="black"):
        line.draw(self.canvas, color)
