import unittest

from maze import Maze


class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._Maze__cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._Maze__cells[0]),
            num_rows,
        )
    
    def test_maze_minimal(self):
        num_cols = 1
        num_rows = 1
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._Maze__cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._Maze__cells[0]),
            num_rows,
        )
        self.assertIsNotNone(m1._Maze__cells[0][0])

    def test_maze_cells(self):
        num_cols = 3
        num_rows = 3
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        center_cell = m1._Maze__cells[1][1]
        self.assertEqual(center_cell._Cell__x1, 10)
        self.assertEqual(center_cell._Cell__y1, 10)
        self.assertEqual(center_cell._Cell__x2, 20)
        self.assertEqual(center_cell._Cell__y2, 20)

    def test_maze_entrance_exit(self):
        num_cols = 3
        num_rows = 3
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        entrance_cell = m1._Maze__cells[0][0]
        exit_cell = m1._Maze__cells[num_cols - 1][num_rows - 1]
        self.assertFalse(entrance_cell.has_top_wall)
        self.assertFalse(exit_cell.has_bottom_wall)
    
    def test_maze_visited_is_cleared(self):
        num_cols = 3
        num_rows = 3
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        for row in m1._Maze__cells:
            for cell in row:
                self.assertFalse(cell.visited)

if __name__ == "__main__":
    unittest.main()
