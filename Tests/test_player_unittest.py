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

    def test_random_player(self):
        print('Testing Random player')
        self.player = PlayerRandom(self.table)
        outcomes = [1,2,3]
        for outcome in outcomes:
            self.player.placeBets()
            for bet in self.table.__iter__():
                print(bet.__repr__())
                if bet.outcome in self.wheel.get(outcome).outcomes:
                    print('Winner')
                    self.player.win(bet)
                else:
                    print('Loser')
                    self.player.lose(bet)
            self.table.clear()
        self.assertEqual(self.player.stake, 185, 'Should be 185')



if __name__ == '__main__':
    unittest.main()
