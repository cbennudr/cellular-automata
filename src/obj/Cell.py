


class Cell:
    def __init__(self, row, col: tuple):
        self.row = row 
        self.col = col
        self.is_alive = False

        self.neighbors = []
        self.history = [] # history of cell being alive/dead

    def __repr__(self):
        # return f"{self.pos}"
        return f"{'alive' if self.is_alive else 'dead'}"

   