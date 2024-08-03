


class Rules:
    def __init__(
            self, 
            min_neighbors_to_stay_alive, 
            max_neighbors_to_stay_alive, 
            min_neighbors_to_come_alive,
            max_neighbors_to_come_alive,

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
            circle_radius=None,
            ):
         
        """
            Rules

            Parameters:
                - min_neighbors_to_stay_alive: the minimum number of alive neighbors for a cell to stay alive
                - max_neighbors_to_stay_alive: the maximum number of alive neighbors for a cell to stay alive
                - min_neighbors_to_come_alive: the minimum number of alive neighbors for a cell to come alive
                
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
                - circle_radius: the radius of the circle around each cell to check
        """
        # Handle no min/max neighbors by setting to number that will always pass condition (see Grid.check_cell_search_area())
        self.min_neighbors_to_stay_alive = min_neighbors_to_stay_alive if min_neighbors_to_stay_alive != None else -1
        self.max_neighbors_to_stay_alive = max_neighbors_to_stay_alive if max_neighbors_to_stay_alive != None else 9999
        self.min_neighbors_to_come_alive = min_neighbors_to_come_alive if min_neighbors_to_come_alive != None else -1
        self.max_neighbors_to_come_alive = max_neighbors_to_come_alive if max_neighbors_to_come_alive != None else 9999
        
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
            self.circle_radius = circle_radius
        else:
            raise ValueError("Invalid search shape")

        