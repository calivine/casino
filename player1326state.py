from bet import Bet


class Player1326State:

    def __init__(self, player):
        self.player = player

    def currentBet(self):
        return NotImplemented

    def nextWon(self):
        return NotImplemented

    def nextLost(self):
        return NotImplemented


class Player1326NoWins(Player1326State):
    def __init__(self, player):
        Player1326State.__init__(self, player)

    def currentBet(self):
        return Bet(self.player.bet * 1, self.player.outcome)

    def nextWon(self):
        return Player1326OneWin(self.player)

    def nextLost(self):
        return Player1326NoWins(self.player)


class Player1326OneWin(Player1326State):
    def __init__(self, player):
        Player1326State.__init__(self, player)

    def currentBet(self):
        return Bet(self.player.bet * 3, self.player.outcome)

    def nextWon(self):
        return Player1326TwoWins(self.player)

    def nextLost(self):
        return Player1326NoWins(self.player)

class Player1326TwoWins(Player1326State):
    def __init__(self, player):
        Player1326State.__init__(self, player)

    def currentBet(self):
        return Bet(self.player.bet * 2, self.player.outcome)

    def nextWon(self):
        return Player1326ThreeWins(self.player)

    def nextLost(self):
        return Player1326NoWins(self.player)


class Player1326ThreeWins(Player1326State):
    def __init__(self, player):
        Player1326State.__init__(self, player)

    def currentBet(self):
        return Bet(self.player.bet * 6, self.player.outcome)

    def nextWon(self):
        return Player1326NoWins(self.player)

    def nextLost(self):
        return Player1326NoWins(self.player)
