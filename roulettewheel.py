import os
import random

from bin import Bin
from outcome import Outcome
from binbuilder import BinBuilder


class Wheel:
    def __init__(self):
        # Create collection of empty Bins
        self.bins = list( Bin([]) for i in range(38) )
        # Set pseudo-random number generator for selecting a winning Bin.
        self.rng = random.Random()
        self.rng.seed()
        self.all_outcomes = {}
        # Fill Bins with possible Outcomes.
        self._fillBins()

    def get(self, number):
        """Retrieves a Bin from the collection of Bins

        Parameters
        -------------
        bin:Int,
        The bin number, in the range of 0,37 inclusive

        Returns
        ----------
            the requested Bin
        """
        return self.bins[number]

    def next(self):
        """Retrieve a Bin based on a randomly generated number between
        0 and 37. Returns the randomly selected Bin.

        Returns
        ----------
        bin:Bin,
            Randomly selected Bin.
        """
        number = self.rng.randint(0,37)
        # self.rng = self.x.randint(0,37)
        # print("Spinning the wheel...\n{}!\n\n\n".format(number))
        return self.bins[number]

    def getOutcome(self, name):
        """Search bins and retrieve an Outcome
        based on the name.

        Parameters
        ------------
        name:String,
            Name of the Outcome to retrieve.

        Returns
        ----------
        outcome:Outcome
        """
        return self.all_outcomes[name]
        # return [oc for oc in self.all_outcomes if oc.lower() == name.lower()]

    def add(self, outcome):
        """Adds outcome to map of all outcomes

        Parameters
        -------------
        outcome:Outcome,
            object to add
        """
        self.all_outcomes[outcome.name] = outcome

    def binIterator(self):
        """Returns an iterator for all bins in the wheel.

        Returns
        ----------
        bins:List
            List of bins to iterate over.
        """
        return self.bins

    def _fillBins(self):
        binBuilder = BinBuilder()

        binBuilder.buildBins(self)
