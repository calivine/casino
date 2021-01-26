from roulettewheel import Wheel
from table import Table
from game import Game
from player import Player, Player57, Martingale, PlayerCancellation
from statistics import IntegerStatistics


class Simulator:

    def __init__(self, game, player):
        """Saves Player and Game instances so we can gather statistics on
        player's betting strategy.
        """
        self.game = game
        self.player = player

        self.initDuration = 50
        self.initStake = 1000
        self.samples = 25
        self.durations = []
        self.maxima = []
        self.round = 0

    def session(self):
        """Executes a single Game session.

        Returns:
        -----------
        stakes:List,
            List of stakes from each session of play.
        """

        self.player.setStake(self.initStake)
        self.player.setRounds(self.initDuration)
        stakes = []
        self.round = 0
        while(self.player.playing() and self.round < self.initDuration):
            if self.player.playing() is None or self.player.playing() == False:
                break
            self.round += 1
            if (isinstance(self.player, PlayerCancellation)):
                self.player.resetSequence()
            #print("Round {:d}".format(self.round))
            #print("Player's stake:{}".format(self.player.stake))
            self.game.cycle(self.player)
            stakes.append(self.player.stake)
        return stakes

    def gather(self):
        """Executes the number of game sessions
        in Samples.
        """
        for i in range(self.samples):
            stakes = self.session()
            self.durations.append(len(stakes))
            self.maxima.append(max(stakes))

    def statistics(self, type):
        """Returns summary statistics about the game simulation.

        Returns:
        -----------
        statistics:List,
            A list of durations or maximum stake values for the Game.
        """
        types = {
            "durations": self.durations,
            "maxima": self.maxima
        }
        print(type)
        print(types[type])
        print("Mean: {}".format(IntegerStatistics(types[type]).mean()))
        print("Std. Deviation: {}\n".format(IntegerStatistics(types[type]).stdDeviation()))
        return types[type]
