
from src.obj.Game import GameOfLife
from src.obj.Rules import Rules
from src.helper.rulesets import CONWAY_RULES, SUPER_BREEDER_CONWAY_RULES
from src.helper.display_attributes import *

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='What the program does')
    ################################################################################
    ''' GENERAL '''
    parser.add_argument('--width', '-w', dest='grid_width', action='store', type=int, required=False, default=100, help="Width of grid")
    parser.add_argument('--height', '-g', dest='grid_height', action='store', type=int, required=False, default=80, help="Height of grid")
    ################################################################################

    ################################################################################
    ''' RULES '''
    parser.add_argument('--conway', dest='conway', action='store_true', required=False, default=False, help="Use rules for Conway's Game of Life")
    parser.add_argument('--super_breeder_conway', dest='super_breeder_conway', action='store_true', required=False, default=False, help="Use rules for Conway's Game of Life with no maximum number of alive neighbors for a dead cell to come alive")
    ################################################################################

    ################################################################################
    ''' DISPLAY SETTINGS '''
    parser.add_argument('--cell_size', '-c', dest='cell_size', action='store', type=int, required=False, default=10, help="Size of cells")
    parser.add_argument('-fps', dest='fps', action='store', type=int, required=False, default=5, help="FPS of game")
    ################################################################################

    args = parser.parse_args()

    if args.conway:
        rules = CONWAY_RULES
    elif args.super_breeder_conway:
        rules = SUPER_BREEDER_CONWAY_RULES
    # Custom rules
    else:
        rules = Rules(
            min_neighbors_to_stay_alive=    args.min_neighbors_to_stay_alive,
            max_neighbors_to_stay_alive=    args.max_neighbors_to_stay_alive,
            min_neighbors_to_come_alive=    args.min_neighbors_to_come_alive,
            max_neighbors_to_come_alive=    args.max_neighbors_to_come_alive,
            search_shape=                   args.search_shape,
            rect_search_x=                  args.rect_search_x,
            rect_search_y=                  args.rect_search_y
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



