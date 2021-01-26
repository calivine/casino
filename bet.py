

class Bet:
    def __init__(self, amount, outcome):
        self.amount = amount
        self.outcome = outcome

    def winAmount(self):
        """Calculate the total prize for the winning Bet.

        Returns
        ----------
        amount:Integer,
            The amount won.
        """
        return self.outcome.winAmount(self.amount) + self.amount

    def loseAmount(self):
        """If Bet is a loser, returns the amount Bet.

        Returns
        ----------
        amount:Integer,
            The amount lost.
        """
        return self.amount

    def __str__(self):
        return "{} on {}".format(self.amount, self.outcome.name)

    def __repr__(self):
        return "{class_:s}({amount!r}, {outcome!r})".format(class_=type(self).__name__, **vars(self))
