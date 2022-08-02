from sudoku_solver.Cell import Cell


class Subgrid:
    cells = [3][3]
    x = None
    y = None

    def __init__(self, x = None, y = None, cells = None):
        if cells is None:
            self.cells = [[Cell(None, None, None) for y in range(3)] for x in range(3)]       
        else:
            self.cells = cells
        self.x = x
        self.y = y  

    def printall(self):
        print("X = " + str(self.x) + "\nY = " + str(self.y))
        for y in range(3):
            for x in range(3):
                print("Value of cell " + str(y) + "-" + str(x) + " = " + str(self.cells[y][x].value))

    
