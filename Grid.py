import numpy as np
from Cell import Cell


class Grid:
    def __init__(self, width: int, height: int, rules):
        self.width = width
        self.height = height

        self.rules = rules
        self.search_shape = self.rules.search_shape

        self.create_grid()
        self.get_cell_neighbors()
        

    def create_grid(self):
        """
            Grid.create_grid: Function to create a numpy array of the specificed grid size where each element is a Cell object
        """
        grid = np.empty((self.height, self.width), dtype=Cell)
        for row in range(self.height):
            for col in range(self.width):
                grid[row][col] = Cell(row, col)
        self.grid = grid


    def get_cell_neighbors(self):
        """
            Grid.get_cell_neighbors: Method to add array of neighbors to each cell
        """

        def get_rect_neighbors(grid, cell, rect_search_y, rect_search_x):
            cells_in_search_area = []

            # Get indices below cell
            for plus_y in range(rect_search_y):
                new_row_inx = cell.row + plus_y+1
                # Ensure not out of bounds
                if new_row_inx > self.grid.shape[0]: break
                cells_in_search_area.append((new_row_inx, cell.col))

            # Get indices above cell
            for minus_y in range(rect_search_y):
                new_row_inx = cell.row - minus_y-1
                # Ensure not out of bounds
                if new_row_inx < 0: break
                cells_in_search_area.append((new_row_inx, cell.col))

            # Get indices to the left of cell
            for minus_x in range(rect_search_x):
                new_col_inx = cell.col - minus_x-1
                # Ensure not out of bounds
                if new_col_inx < 0: break
                cells_in_search_area.append((cell.row, new_col_inx))

            # Get indices to the right of cell
            for plus_x in range(rect_search_x):
                new_col_inx = cell.col + plus_x+1
                # Ensure not out of bounds
                if new_col_inx > self.grid.shape[1]: break
                cells_in_search_area.append((cell.row, new_col_inx))

            raise Exception
            #############################
            # LEFT OFF HERE - NEED TO GET CORNER NEIGHBORS
            #############################

            return cells_in_search_area

        # Go through each cell and create a list of the cells in their serach area
        for row_inx in range(self.grid.shape[0]):
            for col_inx in range(self.grid[row_inx].shape[0]):
                cell = self.grid[row_inx][col_inx]
                if self.search_shape == 'rect':
                    cells_in_search_area = get_rect_neighbors(self.grid, cell, self.rules.rect_search_y, self.rules.rect_search_x)

                elif self.search_shape == 'custom_rect':
                    raise NotImplementedError
                elif self.search_shape == 'circle':
                    raise NotImplementedError
                else:
                    raise ValueError("Invalid search shape")

                cell.neighbors = cells_in_search_area
                    

    def check_cell_search_area(self, cell: Cell) -> bool:
        """
            Grid.check_cell_search_area: Function to check the area in the grid around the provided cell and return True
        """
        pass


    def update(self):
        """
            Grid.update_grid: Method to perform the Game of Life updates
        """
        # Go through each cell and check their list of neighbors
        for row_inx in range(self.grid.shape[0]):
            for col_inx in range(self.grid[row_inx].shape[0]):
                cell = self.grid[row_inx][col_inx]