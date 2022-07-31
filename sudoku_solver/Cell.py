class Cell:
  
    # ATTRIBUTES
    value = None    # Value of the cell
    x = None    # X coordinate of cell in sudoku grid
    y = None    # Y coordinate of cell in sudoku grid
    sub_x = None    # X coordinate of cell in its 3x3 subgrid
    sub_y = None    # Y coordinate of cell in its 3x3 subgrid
    subgrid_x = None    # X coordinate of cell 3x3 subgrid
    subgrid_y = None    # Y coordinate of cell 3x3 subgrid
    candidates = list() # List of all possible candidates


    # METHODS
    # Init methods
    def __init__ (self, value = None, x = None, y = None):
        if value is not None:
            self.value = value
        if x is not None:
            self.x = x
            self.sub_x = x % 3
            self.subgrid_x = x // 3
        if y is not None:
            self.y = y
            self.sub_y = y % 3
            self.subgrid_y = y // 3

    # Print cell attributes
    def printall(self):
        print("Value = " + str(self.value) + "\nX = " + str(self.x) + "\nY = " + str(self.y) + "\nSub X = " + str(self.sub_x) + "\nSub Y = " + str(self.sub_y) + "\nSubgrid X = " + str(self.subgrid_x) + "\nSubgrid Y = " + str(self.subgrid_y))

    
    # Add candidate
    def add_candidate(self, value):
        if value not in self.candidates:    # Checks that the candidate is not already present       
            self.candidates.append(value)
            self.candidates.sort()

    # Remove candidate
    def remove_candidate(self, value):
        if value in self.candidates:    # Check that the candidate exists
            self.candidates.remove(value)
            self.candidates.sort()

    # Set a cell value
    def set_value(self, value):
        if self.value == None:  # Check that value is not already set
            self.value = value
            self.candidates.clear()
