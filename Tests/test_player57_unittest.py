import unittest
import sys

sys.path.append('../')

from table import Table
from validator import InvalidBet
from roulettewheel import Wheel
from player import Martingale, Player57, SevenReds, PlayerRandom
from game import Game


class TestPlayer(unittest.TestCase):

    wheel = Wheel()
    table = Table(wheel)

    def test_player_57(self):
        print('Testing 57')
        self.player = Player57(self.table)
        self.player.placeBets()
        for bet in self.table.__iter__():
            if bet.outcome in self.wheel.get(2).outcomes:
                self.player.win(bet)
            else:
                self.player.lose(bet)
        self.table.clear()
        self.assertEqual(self.player.stake, 210, 'Should be 210')
        self.player.placeBets()
        for bet in self.table.__iter__():
            if bet.outcome in self.wheel.get(2).outcomes:
                self.player.win(bet)
            else:
                self.player.lose(bet)
        self.table.clear()
        self.assertEqual(self.player.stake, 220, 'Should be 220')



if __name__ == '__main__':
    unittest.main()
