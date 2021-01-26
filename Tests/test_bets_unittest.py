import unittest
import sys

sys.path.append('../')

from outcome import Outcome
from bet import Bet
from bin import Bin
from roulettewheel import Wheel
from binbuilder import BinBuilder

from test_outcome_unittest import TestOutcome


class TestBet(unittest.TestCase):

    bet1 = Bet(10, TestOutcome.oc1)
    bet2 = Bet(25, TestOutcome.oc2)
    bet3 = Bet(10, TestOutcome.oc4)
    bet4 = Bet(1, TestOutcome.oc1)

    def test_bet_win_amount(self):
        self.assertEqual(self.bet1.winAmount(), 360, "Should be 360.")

    def test_bet_lose_amount(self):
        self.assertEqual(self.bet1.loseAmount(), 10, "Should be 10.")

    def test_str(self):
        self.assertEqual(self.bet1.__str__(), "10 on 0", "Should be 10 on 0")

    def test_repr(self):
        self.assertEqual(self.bet1.__repr__(), "Bet(10, Outcome('0', 35))", "Should be Bet(10, Outcome(0, 35))")


if __name__ == '__main__':
    unittest.main()
