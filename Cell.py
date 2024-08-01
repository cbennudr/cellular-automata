


class Cell:
    def __init__(self, pos: tuple):
        self.pos = pos # x,y
        self.is_alive = False

        self.history = [] # history of cell being alive/dead

    def __repr__(self):
        # return f"{self.pos}"
        return f"{'alive' if self.is_alive else 'dead'}"

   