import numpy as np
from Cell import Cell

class Grid:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

        self.create_grid()

    def create_grid(self):
        """
            create_grid: Function to create a numpy array of the specificed grid size where each element is a Cell object
        """
        grid = np.empty((self.height, self.width), dtype=Cell)
        for row in range(self.height):
            for col in range(self.width):
                grid[row][col] = Cell((row, col))
        self.grid = grid

    def set_cell_search_area(
            self, 
            search_shape: str, 
            # Rect
            rect_search_y=None,
            rect_search_x=None,
            # Custom rect
            custom_rect_search_left=None, 
            custom_rect_search_right=None, 
            custom_rect_search_up=None, 
            custom_rect_search_down=None,
            # Circle
            radius=None, 
            ):
        
        """
            set_cell_search_area: Function to set the area around each cell to check 

            Parameters:
                - search_shape: the shape of the area to search around a cell - one of 'rect', 'custom_rect', 'circle'
                
                ## For search_shape='rect'
                - rect_search_y: the number of cells above and below of each cell to check 
                - rect_search_x: the number of cells to the left and right of a given cell to check
                ## For search_shape='custom_rect'
                - custom_rect_search_left: the number of cells to the left of each cell to check
                - custom_rect_search_right: the number of cells to the right of each cell to check
                - custom_rect_search_up: the number of cells above each cell to check
                - custom_rect_search_down: the number of cells below each cell to check
                ## For search_shape='circle'
                - radius: the radius of the circle around each cell to check
        """
        
        self.search_shape = search_shape

        if self.search_shape == 'rect':
            self.rect_search_y = rect_search_y
            self.rect_search_x = rect_search_x
        elif self.search_shape == 'custom_rect':
            self.custom_rect_search_left = custom_rect_search_left
            self.custom_rect_search_right = custom_rect_search_right
            self.custom_rect_search_up = custom_rect_search_up
            self.custom_rect_search_down = custom_rect_search_down
        elif self.search_shape == 'circle':
            self.radius = radius
        else:
            raise ValueError("Invalid search shape")


    def check_cell_search_area(self, cell: Cell) -> bool:
        """
            check_cell_search_area: Function to check the area in the grid around the provided cell and return True
        """
        pass