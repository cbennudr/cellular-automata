# Cellular Automata

An implementation of cellular automata

## Usage

Run Conway's Game of Life:  `python run_cellular_automata.py --conway`

**Controls**
- Click cells to activate/deactivate them
- Press *space* to pause/unpause the game
- Press *rightarrow* to step forward
- Press *c* to restart
- Press *q* to quit


### Rulesets

There are a few predefined rulesets in *src/helper/rulesets.py* but you are also able to make your own.

**Preset ruleset arguments**
* **conway** - use the ruleset for Conway's Game of Life
* **super_breeder_conway** - use a similar ruleset to Conway's Game of Life that results in more growth

**Custom ruleset arguments**

* **min_neighbors_to_stay_alive** - the minimum number of alive cells in each cell's search area for an alive cell to stay alive
* **max_neighbors_to_stay_alive** - the maximum number of alive cells in each cell's search area for an alive cell to stay alive
* **min_neighbors_to_come_alive** - the minimum number of alive cells in each cell's search area for a dead cell to come alive
* **max_neighbors_to_come_alive** - the maximum number of alive cells in each cell's search area for a dead cell to come alive
* **search_shape** - one of [rect, custom_rect, circle] that defines the shape of the area around each cell to look for alive/dead neighbors

* *Custom ruleset shape specific arguments* (arguments specifically for each search shape)
    - rect
        * **rect_search_x** - the number of cells to the left/right for each cell to check
        * **rect_search_y** - the number of cells above/below each cell to check 
    - custom_rect
        * TODO (NOT YET IMPLEMENTED)
    - circle
        * **circle_radius** - the radius of the circle around each cell to check (NOT YET IMPLEMENTED)

For example, the following is the 'custom' ruleset that would implement Conway's Game of Life:
``` Shell
python run_cellular_automata.py \
--min_neighbors_to_stay_alive 2 \
--max_neighbors_to_stay_alive 2 \
--min_neighbors_to_come_alive 3 \
--max_neighbors_to_come_alive 3 \
--search_shape rect \
--rect_search_x 1 \
--rect_search_y 1 
```
