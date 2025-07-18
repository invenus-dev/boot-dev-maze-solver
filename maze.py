import random
import time
from cell import Cell
from point import Point
from window import Window

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win: Window = None, seed = None):
        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__win = win
        self.__cells = []
        self.__seed = random.seed(seed) if seed is not None else None
        self.__create_cells()
        self.__break_entrance_and_exit()
        self.__break_walls_r(0, 0)
        self.__reset_cells_visited()
        

    def __create_cells(self):
        for row in range(self.__num_cols):
            col_cells = []
            for j in range(self.__num_rows):
                col_cells.append(Cell(self.__win))
            self.__cells.append(col_cells)
        for i in range(self.__num_cols):
            for j in range(self.__num_rows):
                self.__draw_cell(i, j)

        
    def __draw_cell(self, i, j):
        x1 = self.__x1 + i * self.__cell_size_x
        y1 = self.__y1 + j * self.__cell_size_y
        x2 = x1 + self.__cell_size_x
        y2 = y1 + self.__cell_size_y
        self.__cells[i][j].draw(x1, y1, x2, y2)
        self.__animate()

    def __animate(self):
        if self.__win is None:
            return
        self.__win.redraw()
        time.sleep(0.001)

    def __break_entrance_and_exit(self):
        self.__cells[0][0].has_top_wall = False
        self.__draw_cell(0, 0)    
        self.__cells[self.__num_cols - 1][self.__num_rows - 1].has_bottom_wall = False
        self.__draw_cell(self.__num_cols - 1, self.__num_rows - 1)

    def __break_walls_r(self, i, j):
        current_cell = self.__cells[i][j]
        current_cell.visited = True
        while True:
            to_visit = []
            # check on top
            if j > 0 and not self.__cells[i][j - 1].visited:
                to_visit.append((i, j - 1, "top"))
            # check on bottom
            if j < self.__num_rows - 1 and not self.__cells[i][j + 1].visited:
                to_visit.append((i, j + 1, "bottom"))
            # check on left
            if i > 0 and not self.__cells[i - 1][j].visited:
                to_visit.append((i - 1, j, "left"))
            # check on right
            if i < self.__num_cols - 1 and not self.__cells[i + 1][j].visited:
                to_visit.append((i + 1, j, "right"))
            
            if len(to_visit) == 0:
                return

            # choose random cell to visit
            next_cell_coords = to_visit[random.randint(0, len(to_visit) - 1)]
            next_cell = self.__cells[next_cell_coords[0]][next_cell_coords[1]]
            direction = next_cell_coords[2]

            # knock down walls between current cell and next cell
            if direction == "top":
                current_cell.has_top_wall = False
                next_cell.has_bottom_wall = False
            elif direction == "bottom":
                current_cell.has_bottom_wall = False
                next_cell.has_top_wall = False
            elif direction == "left":
                current_cell.has_left_wall = False
                next_cell.has_right_wall = False
            elif direction == "right":
                current_cell.has_right_wall = False
                next_cell.has_left_wall = False

            self.__draw_cell(i, j)
            self.__draw_cell(next_cell_coords[0], next_cell_coords[1])    

            # move to next cell
            self.__break_walls_r(next_cell_coords[0], next_cell_coords[1])
    
    def __reset_cells_visited(self):
        for i in range(self.__num_cols):
            for j in range(self.__num_rows):
                self.__cells[i][j].visited = False
    
    def solve(self):
        return self.__solve_r(0, 0)
    
    def __solve_r(self, i, j):
        self.__animate()
        current_cell = self.__cells[i][j]
        current_cell.visited = True

        # reached end?
        if i == self.__num_cols - 1 and j == self.__num_rows - 1:
            return True

        # for each direction, check if we can move
        # top
        if j > 0 and not current_cell.has_top_wall and not self.__cells[i][j - 1].visited:
            current_cell.draw_move(self.__cells[i][j - 1], undo=False)
            if self.__solve_r(i, j - 1):
                return True
            else:
                current_cell.draw_move(self.__cells[i][j - 1], undo=True)
        
        # bottom
        if j < self.__num_rows - 1 and not current_cell.has_bottom_wall and not self.__cells[i][j + 1].visited:
            current_cell.draw_move(self.__cells[i][j + 1], undo=False)
            if self.__solve_r(i, j + 1):
                return True
            else:
                current_cell.draw_move(self.__cells[i][j + 1], undo=True)   
        
        # left
        if i > 0 and not current_cell.has_left_wall and not self.__cells[i - 1][j].visited:
            current_cell.draw_move(self.__cells[i - 1][j], undo=False)
            if self.__solve_r(i - 1, j):
                return True
            else:
                current_cell.draw_move(self.__cells[i - 1][j], undo=True)

        # right
        if i < self.__num_cols - 1 and not current_cell.has_right_wall and not self.__cells[i + 1][j].visited:
            current_cell.draw_move(self.__cells[i + 1][j], undo=False)
            if self.__solve_r(i + 1, j):
                return True
            else:
                current_cell.draw_move(self.__cells[i + 1][j], undo=True)

        # no way to go, backtrack
        return False