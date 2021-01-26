import unittest
import sys

sys.path.append('../')

from table import Table
from validator import InvalidBet
from roulettewheel import Wheel
from player import PlayerFibonacci
from game import Game

class TestWheel(unittest.TestCase):
    wheel = Wheel()
    table = Table(wheel)
    player = PlayerFibonacci(table)

    def test_player_fibonacci(self):
        outcomes = [1,1,1,1,2,1,1,1,1,2,1,1,1,1,2]
        for outcome in outcomes:
            self.player.placeBets()
            for bet in self.table.__iter__():
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
