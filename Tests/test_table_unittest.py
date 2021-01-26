import unittest
import sys

sys.path.append('../')
from table import Table
from validator import InvalidBet
from roulettewheel import Wheel

from test_bets_unittest import TestBet


class TestTable(unittest.TestCase):
    wheel = Wheel()
    # table = Table(self.wheel)
    def setUp(self):
        self.table = Table(self.wheel)

    def test_excep(self):
        with self.assertRaises(InvalidBet):
            self.table.placeBet(TestBet.bet4)



if __name__ == '__main__':
    unittest.main()
