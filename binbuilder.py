from roulettegame import RouletteGame
from outcome import Outcome


class BinBuilder:
    def __init__(self):
        pass


    def buildBins(self, wheel):
        """
            buildBins

            Creates the Outcome instances and populates appropriate Bins
            in the Wheel.

            Parameters:
                - wheel (Wheel) - The wheel with bins that must be
                populated with outcomes.

        """
        self.wheel = wheel
        self._fillBins()

        self.wheel.bins = tuple(self.wheel.bins)
        wheel = self.wheel


    def _straighBets(self):
        """
            Generating Straight Bets
        """
        betOdds = RouletteGame.straightBet

        straight = "{}"

        self.wheel.add(Outcome(straight.format(0), betOdds))
        self.wheel.bins[0].addOutcome(Outcome(straight.format(0), betOdds))

        for n in range(1,37):
            self.wheel.bins[n].addOutcome(Outcome(straight.format(n), betOdds))
            self.wheel.add(Outcome(straight.format(n), betOdds))

        self.wheel.bins[37].addOutcome(Outcome(straight.format("00"), betOdds))
        self.wheel.add(Outcome(straight.format("00"), betOdds))


    def _streetBets(self):
        """
            Generating Street Bets
        """
        street = "{0}, {0} + 1, {0} + 2"
        for r in range(12):
            n = 3 * r + 1
            for i in range(n, n+3):
                self.wheel.bins[n].addOutcome(Outcome(street.format(n), RouletteGame.streetBet))
            # self.wheel.bins[n+1].addOutcome(Outcome(street.format(n), RouletteGame.streetBet))
            # self.wheel.bins[n+2].addOutcome(Outcome(street.format(n), RouletteGame.streetBet))

            self.wheel.add(Outcome(street.format(n), RouletteGame.streetBet))


    def _splitBets(self):
        """
            Generating Split Bets
        """
        left_right = "{0}, {0} + 1"
        splitBet = RouletteGame.splitBet
        # Left-Right Pairs
        for r in range(12):
            n = 3 * r + 1

            self.wheel.bins[n].addOutcome(Outcome(left_right.format(n), RouletteGame.splitBet))
            self.wheel.bins[n+1].addOutcome(Outcome(left_right.format(n), RouletteGame.splitBet))


            self.wheel.add(Outcome(left_right.format(n), RouletteGame.splitBet))
            n = 3 * r + 2
            ## print("{} = 3 * {} + 2".format(n, r))
            self.wheel.bins[n].addOutcome(Outcome(left_right.format(n), RouletteGame.splitBet))
            self.wheel.bins[n+1].addOutcome(Outcome(left_right.format(n), RouletteGame.splitBet))

            self.wheel.add(Outcome(left_right.format(n), RouletteGame.splitBet))
            n = 3 * r + 1
            ## print("{} = 3 * {} + 1".format(n, r))


        up_down = "{0}, {0} + 3"
        # Up-Down Pairs
        for n in range(1,34):
            self.wheel.bins[n].addOutcome(Outcome(up_down.format(n), RouletteGame.splitBet))
            self.wheel.bins[n+3].addOutcome(Outcome(up_down.format(n), RouletteGame.splitBet))

            self.wheel.add(Outcome(up_down.format(n), RouletteGame.splitBet))


    def _cornerBets(self):
        """
            Generating Corner Bets
        """
        for r in range(11):
            # First Column Number
            n = 3 * r + 1
            # Column 1-2 Corner
            corner = "{0}, {0} + 1, {0} + 3, {0} + 4".format(n)
            # Assign to Bins.
            for i in range(n, n+5):
                self.wheel.bins[n].addOutcome(Outcome(corner, RouletteGame.cornerBet))
            # self.wheel.bins[n+1].addOutcome(Outcome(corner, RouletteGame.cornerBet))
            # self.wheel.bins[n+3].addOutcome(Outcome(corner, RouletteGame.cornerBet))
            # self.wheel.bins[n+4].addOutcome(Outcome(corner, RouletteGame.cornerBet))
            self.wheel.add(Outcome(corner, RouletteGame.cornerBet))
            # Second Column Number
            n = 3 * r + 2
            # Column 2-3 Corner
            corner = "{0}, {0} + 1, {0} + 3, {0} + 4".format(n)
            # Assign to Bins
            for i in range(n, n+5):
                self.wheel.bins[i].addOutcome(Outcome(corner, RouletteGame.cornerBet))
            # self.wheel.bins[n+1].addOutcome(Outcome(corner, RouletteGame.cornerBet))
            # self.wheel.bins[n+3].addOutcome(Outcome(corner, RouletteGame.cornerBet))
            # self.wheel.bins[n+4].addOutcome(Outcome(corner, RouletteGame.cornerBet))

            self.wheel.add(Outcome(corner, RouletteGame.cornerBet))


    def _lineBets(self):
        """
            Generating Line Bets
        """
        for r in range(11):
            # First Column Number
            n = 3 * r + 1
            line = "{0}, {0} + 1, {0} + 2, {0} + 3, {0} + 4, {0} + 5".format(n)
            # Assign to Bins
            for i in range(n, n+6):
                self.wheel.bins[n].addOutcome(Outcome(line, RouletteGame.lineBet))


            self.wheel.add(Outcome(line, RouletteGame.lineBet))



    def _dozenBets(self):
        """
            Generating Dozen Bets
        """
        for d in range(3):
            dozen = "{} + 1".format(d)
            outcome = Outcome(dozen, RouletteGame.dozenBet)
            self.wheel.add(outcome)
            for m in range(12):
                self.wheel.bins[(12*d)+m+1].addOutcome(outcome)


    def _columnBets(self):
        """
            Generating Column Bets
        """
        for c in range(3):
            column = "{} + 1".format(c)
            outcome = Outcome(column, 2)
            self.wheel.add(outcome)
            for r in range(12):
                self.wheel.bins[3*r+c+1].addOutcome(outcome)



    def _evenMoneyBets(self):
        """
            Generating Even-Money Bets
        """
        evenMoneyBets = {
            "RED" : Outcome("red", 1),
            "BLACK" : Outcome("black", 1),
            "EVEN" : Outcome("even", 1),
            "ODD" : Outcome("odd", 1),
            "HIGH" : Outcome("high", 1),
            "LOW" : Outcome("low", 1)
        }


        bets = evenMoneyBets.values()
        for bet in bets:
            self.wheel.add(bet)


        RED_NUMS = frozenset({1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36})

        for n in range(1,37):
            if n < 19:
                self.wheel.bins[n].addOutcome(evenMoneyBets["LOW"])
            else:
                self.wheel.bins[n].addOutcome(evenMoneyBets["HIGH"])
            if n % 2 == 0:
                self.wheel.bins[n].addOutcome(evenMoneyBets["EVEN"])
            else:
                self.wheel.bins[n].addOutcome(evenMoneyBets["ODD"])
            if n in RED_NUMS:
                self.wheel.bins[n].addOutcome(evenMoneyBets["RED"])
            else:
                self.wheel.bins[n].addOutcome(evenMoneyBets["BLACK"])

    def _fillBins(self):
        self._straighBets()
        self._streetBets()
        self._cornerBets()
        self._splitBets()
        self._lineBets()
        self._dozenBets()
        self._columnBets()
        self._evenMoneyBets()
