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


    def test_martingale(self):
        print('Testing martingale')
        outcomes = [1,1,1,2,2]
        self.player = Martingale(self.table)

        for outcome in outcomes:
            self.player.placeBets()
            for bet in self.table.__iter__():
                print(bet.__repr__())
                if bet.outcome in self.wheel.get(outcome).outcomes:
                    print('Winner')
                    self.player.win(bet)
                else:
                    self.player.lose(bet)
                    print('Loser')
            self.table.clear()
        self.assertEqual(self.player.stake, 255, 'Should be 255')


    def test_seven_reds(self):
        print('Testing SevenReds')
        self.player = SevenReds(self.table)
        outcomes = [1,3,1,1,3,3,3,1,2,1,1,2,2,1,1,1,1,1,1,1,1]
        for outcome in outcomes:
            if self.player.isBetting():

                self.player.placeBets()
                for bet in self.table.__iter__():
                    print(bet.__repr__())
                    if bet.outcome in self.wheel.get(outcome).outcomes:
                        print('Winner')
                        self.player.win(bet)
                    else:
                        print('Loser')
                        self.player.lose(bet)
            self.player.winners(self.wheel.get(outcome).outcomes)
            self.table.clear()

        self.assertEqual(self.player.stake, 185, 'Should be 185')


if __name__ == '__main__':
    unittest.main()
