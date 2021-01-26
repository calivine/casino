import sys


class Outcome:

	def __init__(self, name, odds):
		self.name=name
		self.odds=odds

	def winAmount(self, amount):
		"""Calculate winnings which is: odds * amount Bet.

		Parameters
		-------------
		amount:Integer,
			The amount Bet.

		Returns
		----------
		Amount won.
		"""
		return self.odds * amount

	def __hash__(self):
		return hash(self.name)%sys.hash_info.width

	def __eq__(self, other):
		# Check for equality between Outcomes.
		return hash(self.name) == hash(other.name)

	def __ne__(self, other):
		return self.__hash__() != other.__hash__()

	def __str__(self):
		return "{name:s} ({odds:d}:1)".format_map(vars(self))

	def __repr__(self):
		return "{class_:s}({name!r}, {odds!r})".format(class_=type(self).__name__, **vars(self))
