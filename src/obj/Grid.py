import numpy as np
from src.obj.Cell import Cell


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
            """
                get_rect_neighbors: Function for getting all of the neighboring cells of a cell when searching a rectangular area
            """
            cells_in_search_area = []
            cur_cell_pos = (cell.row, cell.col)
            # Right/Down
            for plus_x in range(rect_search_x+1):
                new_col_inx = cell.col + plus_x
                if new_col_inx >= self.grid.shape[1]: continue
                for plus_y in range(rect_search_y+1):
                    new_row_inx = cell.row + plus_y
                    if new_row_inx >= self.grid.shape[0]: continue
                    cells_in_search_area.append((new_row_inx, new_col_inx))
            # Right/Up
            for plus_x in range(rect_search_x+1):
                new_col_inx = cell.col + plus_x
                if new_col_inx >= self.grid.shape[1]: continue
                for minus_y in range(rect_search_y+1):
                    new_row_inx = cell.row - minus_y
                    if new_row_inx < 0: continue
                    cells_in_search_area.append((new_row_inx, new_col_inx))
            # Left/Down
            for minus_x in range(rect_search_x+1):
                new_col_inx = cell.col - minus_x
                if new_col_inx < 0: continue
                for plus_y in range(rect_search_y+1):
                    new_row_inx = cell.row + plus_y
                    if new_row_inx >= self.grid.shape[0]: continue
                    cells_in_search_area.append((new_row_inx, new_col_inx))
            # Left/Up 
            for minus_x in range(rect_search_x+1):
                new_col_inx = cell.col - minus_x
                if new_col_inx < 0: continue
                for minus_y in range(rect_search_y+1):
                    new_row_inx = cell.row - minus_y
                    if new_row_inx < 0: continue
                    cells_in_search_area.append((new_row_inx, new_col_inx))
            
            # Remove duplicates and the cell being searched for
            cells_in_search_area = sorted([pt for pt in set(cells_in_search_area) if pt != cur_cell_pos])

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
            Grid.check_cell_search_area: Method to check the area in the grid around the provided cell and return whether or not the cell should be alive on the next update

            Returns
                True if the cell should be alive on next update
                False if the cell should be dead on next update
        """
        # Create array of alive/dead bools for neighbor cells
        neighboring_cells_states = []
        for neighbor_cell_pos in cell.neighbors:
            row, col = neighbor_cell_pos
            neighboring_cells_states.append(self.grid[row][col].is_alive)

        alive_neighbors, dead_neighbors = neighboring_cells_states.count(True), neighboring_cells_states.count(False)
        # If cell is alive, check whether it will die or stay alive
        if cell.is_alive:
            if (alive_neighbors >= self.rules.min_neighbors_to_stay_alive) and (alive_neighbors <= self.rules.max_neighbors_to_stay_alive):
                return True
            else:
                return False
        # If cell is dead, check if it is able to come alive
        else:
            if (alive_neighbors >= self.rules.min_neighbors_to_come_alive) and (alive_neighbors <= self.rules.max_neighbors_to_come_alive):
                return True
            else:
                return False


    def update(self):
        """
            Grid.update_grid: Method to perform the Game of Life updates
        """
        # Go through each cell and check their list of neighbors
        for row_inx in range(self.grid.shape[0]):
            for col_inx in range(self.grid[row_inx].shape[0]):
                cell = self.grid[row_inx][col_inx]
                alive_on_next_update = self.check_cell_search_area(cell)
                cell.history.append(alive_on_next_update)
        # Only update cell state after all cells have had their positions checked
        for row_inx in range(self.grid.shape[0]):
            for col_inx in range(self.grid[row_inx].shape[0]):
                cell = self.grid[row_inx][col_inx]
                cell.is_alive = cell.history[-1]