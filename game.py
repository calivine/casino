from roulettewheel import Wheel
from table import Table
from player import Player57


class Game:

    def __init__(self, wheel, table):
        """Create the Game state.

        Parameters
        -------------
        wheel:Wheel,
            Roulette wheel.
        table:Table,
            Game table. Holds the Bets
        """
        self.wheel = wheel
        self.table = table

    def cycle(self, player):
        """Play a round of the game.

        Parameters
        ------------
        player:Player,
            The Player state for the Game.
        """
        # Place bet.
        player.placeBets()

        # Spin the Wheel
        # Returns a Bin.
        winningBin = self.wheel.next()

        # SevenReds:
        # self.player.winners(winningBin.outcomes)

        # Check if Player placed a winning Bet.
        for bet in self.table.__iter__():
            if bet.outcome in winningBin.outcomes:
                # print("Winning bet: {}".format(bet.__str__()))
                player.win(bet)
            else:
                player.lose(bet)
        self.table.clear()
