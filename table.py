import sys


from validator import InvalidBet


class Table:

    def __init__(self, wheel):
        """Game Table state. Tracks table limit, minimum bet,
        and Bets placed by the Player.
        """
        self.limit = 5000
        self.minimum = 5
        self.bets = []
        self.wheel = wheel

    def getWheel(self):
        """Returns the table's wheel object.

        Returns:
        -----------
        wheel:Wheel
            The Wheel which holds bins and outcomes.
        """
        return self.wheel

    def placeBet(self, bet):
        """Adds a Bet to the Table's collection of Bets.

        Parameters
        -------------
        bet:Bet,
            The Bet being placed.
        """
        # Confirm that Bet's Outcome exists in a Bin.
        try:
            self.isValid(bet)
            self.bets.append(bet)
        except InvalidBet as e:
            # print("InvalidBet: {}".format(e))
            pass
        except:
            print("Unexpected error:", sys.exc_info()[0])
            raise

    def __iter__(self):
        """Get an iterable object of the Bins.

        Returns
        ---------
            Iterator of Bins
        """
        return self.bets[:]

    def __str__(self):
        """Returns a string representation of the Table's Bets.

        Returns
        ----------
            String representation of the Bets.
        """
        l = []
        for s in self.bets:
            l.append(s.__str__())

        contents = ', '.join(l)
        return '['+contents+']'

    def __repr__(self):
        return "{class_:s}({bets_:s})".format(class_=type(self).__name__, bets_=self.__str__())

    def isValid(self, bet):
        """Extends Exception to check that a valid Bet has been placed.
        Raise InvalidBet Exception if illegal Bet is placed
        Parameters
        ------------
        bet:Bet,
            The Bet being placed.
        """
        potentialWinnings = 0
        # Check that Bet is greater than or equal to Min Bet
        for b in self.bets:
            potentialWinnings += b.winAmount()
        potentialWinnings += bet.winAmount()
        if potentialWinnings > self.limit:
            raise InvalidBet("Bet is too high.")
        elif bet.amount < self.minimum:
            raise InvalidBet("Bet is less than the minimum table bet.")

    def clear(self):
        """Clears the Table of Bets.
        """
        self.bets.clear()
