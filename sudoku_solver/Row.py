from sudoku_solver.Cell import Cell


class Row:
    cells = list()
    y = None

    def __init__(self, y = None, cells = None):
        if cells is None:
            self.cells = [Cell(None, None, None) for index in range(9)]
            self.y = y         
        else:
            self.cells = cells
            self.y = y       

    def printall(self):
        print("Y = " + str(self.y))
        for index, cell in enumerate(self.cells):
            print("Value of cell " + str(index) + " = " + str(cell.value))

    def add_cell(self, cell):
        if len(self.cells) < 9:
            self.cells.append(cell)
    
