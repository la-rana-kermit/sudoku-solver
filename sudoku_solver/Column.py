from sudoku_solver.Cell import Cell


class Column:
    cells = list()
    x = None

    def __init__(self, x, cells = None):
        if cells is None:
            self.cells = [Cell(None, None, None) for index in range(9)]
            self.x = x          
        else:
            self.cells = cells
            self.x = x        

    def printall(self):
        print("X = " + str(self.x))
        for index, cell in enumerate(self.cells):
            print("Value of cell " + str(index) + " = " + str(cell.value))

    def add_cell(self, cell):
        if len(self.cells) < 9:
            self.cells.append(cell)
    
