from components.players import MoonwalkerPlayer, DoubloonPlayer, TripettePlayer, TatersPlayer
import random

class Record:

	def __init__(self):
		self.wins = 0
		self.loses = 0
		self.ties = 0

	def win_percentage(self):
		return (self.wins + 0.5*self.ties)/self.total_games() 

	def total_games(self):
		return self.wins + self.loses + self.ties

class Lineup:

	def __init__(self, players):
		self.players = players
		self.record = Record()
		self.total_score = 0

	def top_of_inning(self):
		for player in self.players:
			player.base = 0

	def average_score(self):
		return self.total_score/self.record.total_games()

def create_fully_random_lineup(size, double_perc, hr_perc, walk_perc, trip_perc):
	lineup = [randomly_select_player(double_perc, hr_perc, walk_perc, trip_perc) for i in range(size)]
	return Lineup(lineup)

def randomly_select_player(double_perc, hr_perc, walk_perc, trip_perc):
	rand_val = random.random()
	if (rand_val < 1/4):
		return DoubloonPlayer(double_perc)
	elif (rand_val < 2/4):
		return TatersPlayer(hr_perc)
	elif (rand_val < 3/4):
		return TripettePlayer(trip_perc)
	else:
		return MoonwalkerPlayer(walk_perc)

def randomly_change_players(lineup, num_change, double_perc, hr_perc, walk_perc, trip_perc):
	for i in range(num_change):
		lineup.players[random.randint(0, len(lineup.players)-1)] = randomly_select_player(double_perc, hr_perc, walk_perc, trip_perc)
	return lineup