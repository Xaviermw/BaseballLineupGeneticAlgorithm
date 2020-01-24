import random
import copy
import components.lineup as lu
from components.game import Game
from enum import Enum

class FitMetric(Enum):
	WIN_PERCENTAGE = 0
	AVERAGE_SCORE = 1

class GeneticRound:

	def __init__(self, parents, num_mutations, lineup_size, double_perc, hr_perc, walk_perc, trip_perc, innings_in_game, seasons_played, fit_metric):
		self.double_perc = double_perc
		self.hr_perc = hr_perc
		self.walk_perc = walk_perc
		self.trip_perc = trip_perc
		self.lineup_size = lineup_size
		self.innings_in_game = innings_in_game
		self.seasons_played = seasons_played
		self.parents = parents
		self.num_mutations = num_mutations
		self.fit_metric = fit_metric
		self.mutants = []
		self.children = []
		self.all_lineups = []
		self.best_lineups = []
		self.clear_records()
		self.append_to_all(parents)

	def clear_records(self):
		for parent in self.parents:
			parent.record = lu.Record()
			parent.total_score = 0

	def create_mutants(self):
		self.mutants = [self.create_a_mutant() for i in range(len(self.parents))]
		self.append_to_all(self.mutants)

	def create_a_mutant(self):
		random_parent = random.randint(0, len(self.parents)-1)
		parent_copy = copy.deepcopy(self.parents[random_parent])
		return lu.randomly_change_players(parent_copy, self.num_mutations, self.double_perc, self.hr_perc, self.walk_perc, self.trip_perc)

	def create_children(self):
		self.children = [self.create_a_child() for i in range(len(self.parents))]
		self.append_to_all(self.children)

	def create_a_child(self):
		split_location = random.randint(1, self.lineup_size-1)
		first_strand = copy.deepcopy(self.parents[random.randint(0, len(self.parents)-1)].players[:split_location])
		second_strand = copy.deepcopy(self.parents[random.randint(0, len(self.parents)-1)].players[split_location:])
		return lu.Lineup(first_strand + second_strand)

	def simulate_lineup_scores(self):
		for season in range(self.seasons_played):
			for home in self.all_lineups:
				for away in self.all_lineups:
					if home != away:
						home_game = Game(self.innings_in_game, home)
						home_game.run_game()
						home_score = home_game.total_score
						home.total_score = home.total_score + home_score
						away_game = Game(self.innings_in_game, away)
						away_game.run_game()
						away_score = away_game.total_score
						away.total_score = away.total_score + away_score
						if home_score == away_score:
							home.record.ties = home.record.ties + 1
							away.record.ties = away.record.ties + 1
						elif home_score > away_score:
							home.record.wins = home.record.wins + 1
							away.record.loses = away.record.loses + 1
						else:
							home.record.loses = home.record.loses + 1
							away.record.wins = away.record.wins + 1

	def calculate_most_fit_lineup(self):

		if (self.fit_metric == FitMetric.WIN_PERCENTAGE):
			self.all_lineups.sort(key=lambda x: x.record.win_percentage(), reverse=True)
		elif (self.fit_metric == FitMetric.AVERAGE_SCORE):
			self.all_lineups.sort(key=lambda x: x.average_score(), reverse=True)
		else:
			raise ValueError("Incorrect Fit Metric Used")

		print("Lineup: " + str(self.all_lineups[0].players))
		print("Win Percentage: " + str(self.all_lineups[0].record.win_percentage()))
		print("Average Score: " + str(self.all_lineups[0].average_score()))
		self.best_lineups = self.all_lineups[:20]

	def append_to_all(self, lineups):
		self.all_lineups = self.all_lineups + lineups