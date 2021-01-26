from roulettewheel import Wheel
from table import Table
from game import Game
from player import Player57, Martingale, SevenReds, PlayerRandom, Player1326, PlayerCancellation, PlayerFibonacci
from simulator import Simulator
from statistics import IntegerStatistics


import random

wheel = Wheel()
table = Table(wheel)

# self.player = Player57(self.table)
# player = SevenReds(table)
print("Random Player")
player = PlayerRandom(table)
game = Game(wheel, table)

simulator = Simulator(game, player)

simulator.gather()
durations = simulator.statistics("durations")
maxima = simulator.statistics("maxima")

print("Seven Reds")
player = SevenReds(table)
simulator = Simulator(game, player)

simulator.gather()
durations = simulator.statistics("durations")
maxima = simulator.statistics("maxima")

print("Player 1326")
player = Player1326(table)
simulator = Simulator(game, player)

simulator.gather()
durations = simulator.statistics("durations")
maxima = simulator.statistics("maxima")

print("Player Cancellation")
player = PlayerCancellation(table)
simulator = Simulator(game, player)

simulator.gather()
durations = simulator.statistics("durations")
maxima = simulator.statistics("maxima")

print("Player Fibonacci")
player = PlayerFibonacci(table)
simulator = Simulator(game, player)

simulator.gather()
durations = simulator.statistics("durations")
maxima = simulator.statistics("maxima")
