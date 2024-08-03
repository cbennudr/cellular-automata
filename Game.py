
import cv2 as cv
import numpy as np
from Grid import Grid


        

class GameOfLife:
    def __init__(self, grid_width, grid_height, rules, cell_size=25):
        self.grid = Grid(grid_width, grid_height, rules)

        self.cell_size = cell_size

        self.display_grid_bg_color              = (128,128,128) # grey
        self.display_grid_cell_outline_color    = (0,0,0,100)
        self.alive_cell_color                   = (0,200,0) # green
        self.dead_cell_color                    = (6,6,150) # red

        self.setup_window()
        self.create_display()


            
    def setup_window(self):
        """
            GameOfLife.setup_window: Method to setup the opencv window for displaying the board
        """
        def set_clicked_cell(mouseX, mouseY):
            cellRow = int(np.floor(mouseY/self.cell_size))
            cellCol = int(np.floor(mouseX/self.cell_size))
            clicked_cell = self.grid.grid[cellRow][cellCol]
            clicked_cell.is_alive = not clicked_cell.is_alive

            # TMP
            print(f"{(clicked_cell.row, clicked_cell.col)}: {clicked_cell.neighbors}")

        def mouse_callback(event, x, y, flags, param):
            if event == cv.EVENT_LBUTTONDOWN:
                set_clicked_cell(x, y)

        # Setup opencv display options
        self.windowname = 'Game of Life'
        cv.namedWindow(self.windowname)
        cv.setMouseCallback(self.windowname, mouse_callback)
    
    def create_display(self):
        """
            GameOfLife.create_display: Method to create empty display board
        """
        # Get size of display 
        self.display_width = self.grid.grid.shape[1] * self.cell_size
        self.display_height = self.grid.grid.shape[0] * self.cell_size

        # Create matrix for display
        display = np.zeros((self.display_height, self.display_width), dtype=np.uint8)
        # For BGR
        display = cv.cvtColor(display, cv.COLOR_GRAY2BGR)
        display[:,:,0], display[:,:,1], display[:,:,2] = self.display_grid_bg_color 

        self.display = display

    def run(self):     
        """
            GameOfLife.run: Method to start running Conway's Game of Life
        """   
        running = True
        while running:
            # Create cells (rects) on the display grid
            for row_inx in range(self.grid.grid.shape[0]):
                for col_inx in range(self.grid.grid[row_inx].shape[0]):
                    # Get top left and bottom right points of cell
                    pt1 = (col_inx*self.cell_size, row_inx*self.cell_size)
                    pt2 = (col_inx*self.cell_size+self.cell_size, row_inx*self.cell_size+self.cell_size)
                    # Draw the appropriate colored rectangle for the cell
                    cell = self.grid.grid[row_inx][col_inx]
                    if cell.is_alive: cv.rectangle(self.display, pt1, pt2, self.alive_cell_color, -1)
                    else: cv.rectangle(self.display, pt1, pt2, self.dead_cell_color, -1)
                    cv.putText(self.display, f"{row_inx},{col_inx}", (pt1[0], int(pt1[1]+self.cell_size/2)), cv.FONT_HERSHEY_COMPLEX_SMALL, .5, (255,0,255), 1)

            cv.imshow(self.windowname, self.display)

            self.grid.update()

            key = cv.waitKey(1)
            if key == ord('q'): 
                running = False
