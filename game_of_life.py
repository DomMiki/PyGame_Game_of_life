import typing
from collections import defaultdict


class GameOfLife:
    """
    Dead cell with 3 neighbours revive
    Living cell with 2 or 3 neighbours is still alive
    Other combination make the cell die
    """
    def __init__(self, seed: typing.Optional[list]=None):
        if seed is not None:
            self.seed = seed
        else:
            raise Exception

    def create_cells(self):
        cell_range = defaultdict(int)
        cells_to_create = []
        for x, y in self.seed:
            for i in list(range(x-1, x+2)):
                for j in list(range(y-1, y+2)):
                    if [i, j] not in self.seed:
                        cell_range[(i, j)] += 1
        for i in cell_range.items():
            if i[1] == 3:
                cells_to_create.append(i[0])
        return cells_to_create

    def destroy_cells(self):
        cell_range = defaultdict(int)
        cells_to_destroy = []
        for x, y in self.seed:
            for i in list(range(x - 1, x + 2)):
                for j in list(range(y - 1, y + 2)):
                    if [i, j] in self.seed and [i, j] != [x, y]:
                        cell_range[(x, y)] += 1
        for i in cell_range.items():
            if i[1] not in (2, 3):
                cells_to_destroy.append(i[0])
        return cells_to_destroy

    def change_the_life(self):
        pass

    def time_lapse(self):
        pass

    def actual_position_of_cells(self):
        pass


if __name__ == '__main__':
    game = GameOfLife([[2, 3], [3, 3], [4, 3]])
    print(game.create_cells())
    print(game.destroy_cells())
    game.change_the_life()

