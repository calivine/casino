import unittest
import sys

sys.path.append('../')
from bet import Bet
from outcome import Outcome
from table import Table
from roulettewheel import Wheel
from player import Player1326
from player1326state import *


from test_bets_unittest import TestBet


class TestPlayer1326State(unittest.TestCase):
    wheel = Wheel()
    table = Table(wheel)
    player = Player1326(table)
    player1326state = Player1326State(player)

    def test_state(self):
        noWins = Player1326NoWins(self.player)
        print(noWins.currentBet())

        self.assertEqual(noWins.currentBet().__repr__(), Bet(1, Outcome('black', 1)).__repr__())

        oneWin = noWins.nextWon()
        print(oneWin.currentBet())

        twoWins = oneWin.nextWon()
        print(twoWins.currentBet())

        threeWins = twoWins.nextWon()
        print(threeWins.currentBet())






if __name__ == '__main__':
    unittest.main()
