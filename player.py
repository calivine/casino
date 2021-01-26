import random

from outcome import Outcome
from bet import Bet
from player1326state import *



class Player:

    def __init__(self, table):
        """Player state. Tracks Player's bets,
        stake, winnings, and actions.
        """
        self.table = table
        self.stake = 200
        self.roundsToGo = 25

    def playing(self):
        if self.roundsToGo == 0:
            return False
        elif self.stake < self.table.minimum:
            return False
        else:
            return True

    def win(self, bet):
        """Notification from the Game that the Bet was a winning Bet.
        Updates Player's stake with winnings.

        Parameters
        -------------
        bet:Bet,
            The winning Bet.

        """
        self.stake += bet.winAmount()

    def lose(self, bet):
        """Notification from the Game that the Bet was a losing Bet.
        Updates Player's stake with amount lost.

        Parameters
        -------------
        bet:Bet,
            The losing Bet.
        """
        self.stake -= bet.loseAmount()

    def placeBets(self):
        pass

    def setStake(self, stake):
        """Sets the player's total stake.

        Parameters:
        --------------
        stake:Integer,
            Player's stake.
        """
        self.stake = stake

    def setRounds(self, rounds):
        """Sets rounds player will play.

        Parameters:
        --------------
        rounds:Integer,
            Cycles of the game.
        """
        self.roundsToGo = rounds

    def winners(self, outcomes):
        pass


class Player57(Player):

    def placeBets(self):
        """Player places a Bet.
        """
        self.table.placeBet(Bet(5, Outcome('black', 1)))


class Martingale(Player):

    def __init__(self, table):
        Player.__init__(self, table)
        self.lossCount = 0
        self.betMultiple = 1

    def placeBets(self):
        self.table.placeBet(Bet(self.betMultiple*5, Outcome('black', 1)))

    def win(self, bet):
        Player.win(self, bet)
        self.lossCount = 0
        self.betMultiple = 1

    def lose(self, bet):
        Player.lose(self, bet)
        self.lossCount += 1
        self.betMultiple *= 2


class SevenReds(Martingale):
    def __init__(self, table):
        Martingale.__init__(self, table)
        self.redsToGo = 7

    def placeBets(self):
        Martingale.placeBets(self)

    def playing(self):
        if self.roundsToGo == 0:
            return False
        elif self.stake < self.table.minimum or self.stake <= 0:
            return False
        else:
            return True

    def isBetting(self):
        return self.redsToGo == 0

    def winners(self, outcomes):
        if Outcome('red', 1) in outcomes:
            self.redsToGo -= 1
        else:
            self.redsToGo = 7

    def win(self, bet):
        Player.win(self, bet)
        self.lossCount = 0
        self.betMultiple = 1
        self.roundsToGo -= 1

    def lose(self, bet):
        Player.lose(self, bet)
        self.lossCount += 1
        self.betMultiple *= 2
        self.roundsToGo -= 1


class PlayerRandom(Player):

    def __init__(self, table):
        Player.__init__(self, table)
        self.outcomes = self._getAllOutcomes()
        self.rng = random.Random()
        self.rng.seed(1)

    def placeBets(self):
        """Updates the table with player's bet.
        """
        bet = self.rng.randrange(0,len(self.outcomes)-1)

        self.table.placeBet(Bet(5, self.outcomes[bet]))

    def win(self, bet):
        Player.win(self, bet)

    def lose(self, bet):
        Player.lose(self, bet)


    def _getAllOutcomes(self):
        wheel = self.table.getWheel()
        all_outcomes_list = []
        for b in wheel.binIterator():
            for o in b.outcomeIterator():
                all_outcomes_list.append(o)
        return all_outcomes_list


class Player1326(Player):

    def __init__(self, table):
        Player.__init__(self, table)
        self.outcome = self.table.getWheel().getOutcome("black")
        self.state = Player1326NoWins(self)
        self.bet = 5

    def placeBets(self):
        self.table.placeBet(self.state.currentBet())

    def win(self, bet):
        Player.win(self, bet)
        self.state = self.state.nextWon()

    def lose(self, bet):
        Player.lose(self, bet)
        self.state = self.state.nextLost()


class PlayerCancellation(Player):

    def __init__(self, table):
        Player.__init__(self, table)
        self.sequence = None
        self.outcome = None
        self.resetSequence()

    def resetSequence(self):
        self.sequence = list(i for i in range(1,7))
        self.outcome = self.table.getWheel().getOutcome("black")

    def placeBets(self):
        if len(self.sequence) != 0:
            self.table.placeBet(Bet(self.sequence[0]+self.sequence[-1], self.outcome))

    def win(self, bet):
        Player.win(self, bet)
        self.sequence = self.sequence[1:-1]

    def lose(self, bet):
        Player.lose(self, bet)
        self.sequence.append(self.sequence[0]+self.sequence[-1])


class PlayerFibonacci(Player):

    def __init__(self, table):
        Player.__init__(self, table)
        self.recent = 1
        self.previous = 0
        self.outcome = self.table.getWheel().getOutcome("black")

    def placeBets(self):
        self.table.placeBet(Bet(self.recent * 5, self.outcome))

    def win(self, bet):
        Player.win(self, bet)
        self.recent = 1
        self.previous = 0

    def lose(self, bet):
        Player.lose(self, bet)
        next = self.recent + self.previous
        self.previous = self.recent
        self.recent = next
