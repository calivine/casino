import unittest
import sys



sys.path.append('../')

from bin import Bin

from test_outcome_unittest import TestOutcome

class TestBin(unittest.TestCase):
    def setUp(self):
        self.bin = Bin([])
        self.bin.addOutcome(TestOutcome.oc1)
        self.bin.addOutcome(TestOutcome.oc2)
        self.outcome1 = TestOutcome.oc1
        self.outcome2 = TestOutcome.oc2
        self.outcome3 = TestOutcome.oc3

    def runBinTest1(self):
        self.assertEqual(self.outcome1 in self.bin.outcomeIterator(), True, "Should be true")

    def runBinTest2(self):
        self.assertEqual(self.outcome2 in self.bin.outcomeIterator(), True, "Should be true")

    def runBinTest3(self):
        self.assertEqual(self.outcome3 in self.bin.outcomeIterator(), False, "Should be false")

if __name__ == '__main__':
    unittest.main()
