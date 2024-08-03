
from Game import GameOfLife
from Rules import Rules

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='What the program does')
    parser.add_argument('--width', '-w', dest='grid_width', action='store', type=int, required=False, default=30, help="Width of grid")
    parser.add_argument('--height', '-g', dest='grid_height', action='store', type=int, required=False, default=20, help="Height of grid")
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
        'cell_size':                            10,
        'display_grid_bg_color':                (128,128,128),
        'display_grid_cell_outline_color':      (0,0,0,0),
        'alive_cell_color':                     (0,200,0),
        'dead_cell_color':                      (6,6,150),
        'fps':                                  5
    }

    Life = GameOfLife(
        grid_width=             args.grid_width,
        grid_height=            args.grid_height,
        rules=                  rules,
        display_settings=       display_settings_dict
    )
    Life.run()



