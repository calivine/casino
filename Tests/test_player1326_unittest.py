import unittest
import sys

sys.path.append('../')

from table import Table
from validator import InvalidBet
from roulettewheel import Wheel
from player import Player1326
from game import Game


class TestPlayer(unittest.TestCase):

    wheel = Wheel()
    table = Table(wheel)
    player = Player1326(table)

    def test_player1326(self):
        outcomes = [2,2,2,2]
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
            print(self.player.stake)
        self.assertEqual(self.player.stake, 320, 'Should be 320')
        outcomes = [1,2,2,1]
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
            print(self.player.stake)
        outcomes = [1,1,2,1]
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
            print(self.player.stake)






if __name__ == '__main__':
    unittest.main()
