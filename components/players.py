from enum import Enum
import random

class Hit(Enum):
	OUT = 0
	SINGLE = 1
	DOUBLE = 2
	TRIPLE = 3
	HR = 4

class Player:

	def __init__(self):
		self.base = 0

class MoonwalkerPlayer(Player):
	def __init__(self, walk_percentage):
		self.walk_percentage = walk_percentage

	def calculate_outcome(self):
		if (random.random() < self.walk_percentage):
			return Hit.SINGLE
		else:
			return Hit.OUT

class DoubloonPlayer(Player):
	def __init__(self, double_percentage):
		self.double_percentage = double_percentage

	def calculate_outcome(self):
		if (random.random() < self.double_percentage):
			return Hit.DOUBLE
		else:
			return Hit.OUT

class TripettePlayer(Player):
	def __init__(self, triple_percentage):
		self.triple_percentage = triple_percentage

	def calculate_outcome(self):
		if (random.random() < self.triple_percentage):
			return Hit.TRIPLE
		else:
			return Hit.OUT

class TatersPlayer(Player):
	def __init__(self, hr_percentage):
		self.hr_percentage = hr_percentage

	def calculate_outcome(self):
		if (random.random() < self.hr_percentage):
			return Hit.HR
		else:
			return Hit.OUT