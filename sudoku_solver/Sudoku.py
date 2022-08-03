from sudoku_solver.Cell import Cell
from sudoku_solver.Column import Column
from sudoku_solver.Row import Row
from sudoku_solver.Subgrid import Subgrid

class Sudoku:
    grid = [[Cell(None, None, None) for y in range(9)] for x in range(9)]
    subgrids = [[Subgrid(None, None, None) for y in range(3)] for x in range(3)]
    rows = [Row(None, None) for index in range(9)]
    columns = [Column(None, None) for index in range(9)]

    def _init__(self, grid = None, subgrids = None, rows = None, columns = None, blank = None):
        if grid is None:
            self.grid = self.autogeneration(blank)
        if subgrids is None and rows is None and columns is None:
            for y in range(9):
                for x in range (9):
                    self.grid[y][x] = Cell(grid[y][x], x, y)
                    self.rows[y].cells[x] = self.grid[y][x]
                    self.columns[x].cells[y] = self.grid[y][x]
                    self.subgrids[self.grid[y][x].subgrid_y][self.grid[y][x].subgrid_x].cells[self.grid[y][x].sub_y][self.grid[y][x].sub_x] = self.grid[y][x]

    def autogeneration(self, blank):
        grid = None
        return grid