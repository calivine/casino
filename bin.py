

class Bin:
    def __init__(self, outcomes):
        self.outcomes = frozenset(outcomes)


    def addOutcome(self, outcome):
        """Adds the given Outcome to the Bin.

        Parameters:
        --------------
        outcome:Outcome,
            The Outcome to add to this Bin
        """
        self.outcomes |= set([outcome])

    def outcomeIterator(self):
        """Returns frozenset representing outcomes.

        Returns:
        ----------
        outcomes:Frozenset
            Set of bin's outcomes. 
        """
        return self.outcomes;
