
from Game import GameOfLife
from Rules import Rules
from display_attributes import *

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='What the program does')
    parser.add_argument('--width', '-w', dest='grid_width', action='store', type=int, required=False, default=100, help="Width of grid")
    parser.add_argument('--height', '-g', dest='grid_height', action='store', type=int, required=False, default=80, help="Height of grid")

    parser.add_argument('--cell_size', '-c', dest='cell_size', action='store', type=int, required=False, default=10, help="Size of cells")
    parser.add_argument('-fps', dest='fps', action='store', type=int, required=False, default=5, help="FPS of game")
    args = parser.parse_args()

    rules = Rules(
        min_neighbors_to_stay_alive=    2,
        max_neighbors_to_stay_alive=    3,
        min_neighbors_to_come_alive=    3,
        search_shape=                   'rect',
        rect_search_x=                  1,
        rect_search_y=                  1
    )

    display_settings_dict = {
        'cell_size':                            args.cell_size,
        'display_grid_bg_color':                DARKGREY,
        'display_grid_cell_outline_color':      None,
        'alive_cell_color':                     GREEN,
        'dead_cell_color':                      DARKBLUE,
        'fps':                                  args.fps
    }

    Life = GameOfLife(
        grid_width=             args.grid_width,
        grid_height=            args.grid_height,
        rules=                  rules,
        display_settings=       display_settings_dict
    )
    Life.run()



