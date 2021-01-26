import unittest
import sys

sys.path.append('../')
from table import Table
from validator import InvalidBet
from roulettewheel import Wheel
from player import Martingale, Player57
from game import Game

class TestGame(unittest.TestCase):

    def setUp(self):
        self.wheel = Wheel()
        self.table = Table(self.wheel)
        self.player = Player57(self.table)
        self.game = Game(self.wheel, self.table)

    def runTest(self):
        self.game.cycle(self.player)
        self.assertEqual(self.player.stake, 210, 'Should be 210.')
        self.game.cycle(self.player)
        self.assertEqual(self.player.stake, 205, 'Should be 205.')
        self.game.cycle(self.player)
        self.assertEqual(self.player.stake, 215, 'Should be 215.')


if __name__ == '__main__':
    unittest.main()
