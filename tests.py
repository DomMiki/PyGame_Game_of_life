import unittest
from .game_of_life import GameOfLife


class TestGameOfLifePrimaryFunction(unittest.TestCase):

    def setUp(self) -> None:
        self.game = GameOfLife([[1, 4], [5, 7], [1, 7]])

    def test_seed_creation(self):
        self.user_seed = [[1, 4], [5, 7], [1, 7]]
        self.assertEqual(self.game.seed, self.user_seed)
