from src.obj.Rules import Rules


CONWAY_RULES = Rules(
    min_neighbors_to_stay_alive=    2,
    max_neighbors_to_stay_alive=    3,
    min_neighbors_to_come_alive=    3,
    max_neighbors_to_come_alive=    3,
    search_shape=                   'rect',
    rect_search_x=                  1,
    rect_search_y=                  1
)

SUPER_BREEDER_CONWAY_RULES = Rules(
    min_neighbors_to_stay_alive=    2,
    max_neighbors_to_stay_alive=    3,
    min_neighbors_to_come_alive=    3,
    max_neighbors_to_come_alive=    None,
    search_shape=                   'rect',
    rect_search_x=                  1,
    rect_search_y=                  1
)