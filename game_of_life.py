import typing
from collections import defaultdict


class GameOfLife:
    """
    Dead cell with 3 neighbours revive
    Living cell with 2, 3 neighbours is still alive
    Other combination make the cell die
    """
    def __init__(self, seed: typing.Optional[list]=None):
        if seed is not None:
            self.seed = seed
        else:
            raise Exception

    def create_cells(self):
        cell_range = defaultdict()
        for coordinates in self.seed:
            for x, y in coordinates:
                for i in range(x+1, x-1):
                    for j in range(y+1, y-1):
                        if [i, j] not in self.seed:
                            cell_range[[i, j]] += 1

    def destroy_cells(self):
        for coordinates in self.seed:
            for x, y in coordinates:
                pass

    def change_the_life(self):
        pass

    def time_lapse(self):
        pass


if __name__ == '__main__':
    game = GameOfLife([[2, 3], [3, 3], [4, 3]])
    game.create_cells()
