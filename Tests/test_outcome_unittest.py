import unittest
import sys


sys.path.append('../')

from outcome import Outcome


class TestOutcome(unittest.TestCase):

    oc1 = Outcome("0", 35)
    oc2 = Outcome("1", 5)
    oc3 = Outcome("2", 1)
    oc4 = Outcome("red", 1)
    oc5 = Outcome("even", 1)
    oc6 = Outcome("odd", 1)

    def test_eq(self):
        self.assertEqual(TestOutcome.oc1.__eq__(TestOutcome.oc2), False , "Should be false.")

    def test_winAmount(self):
        self.assertEqual(TestOutcome.oc1.winAmount(2), 70, "Should be 70")

    def test_ne(self):
        self.assertEqual(TestOutcome.oc3.__ne__(TestOutcome.oc2), True, "Should be false.")

    def test_eq2(self):
        self.assertNotEqual(TestOutcome.oc1.__eq__(TestOutcome.oc3), True, "Should be not equal.")

    def test_str(self):
        self.assertEqual(TestOutcome.oc1.__str__(), "0 (35:1)", "Should be 0 (35:1)")



if __name__ == '__main__':
    unittest.main()
