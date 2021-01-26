from roulettewheel import Wheel
from table import Table
from game import Game
from player import Player57, Martingale


class Play:

    def __init__(self):
        """Initialize Play state by setting Table, Wheel, Player, Game
        """
        self.wheel = Wheel()
        self.table = Table(self.wheel)

        # self.player = Player57(self.table)
        self.player = Martingale(self.table)
        self.game = Game(self.wheel, self.table)

    def run(self):
        """Play round of game.

        Parameters
        -------------
        player:Player,
            Player state for a round of the Game.
        """
        print(self.player.stake)
        if self.player.playing():
            self.game.cycle(self.player)
        print(self.player.stake)
