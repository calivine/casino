import unittest
import sys

sys.path.append('../')

from outcome import Outcome
from bin import Bin
from roulettewheel import Wheel

from test_outcome_unittest import TestOutcome


class TestWheel(unittest.TestCase):
    wheel = Wheel()
    def setUp(self):
        self.winningBin = self.wheel.next().outcomes
        self.oc5 = TestOutcome.oc5

    def runTest(self):
        self.assertEqual(self.oc5 in self.winningBin, True, "Should be true.")


if __name__ == '__main__':
    unittest.main()
