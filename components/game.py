from components.players import Hit

class Inning:

	def __init__(self, lineup, batter_up):
		self.lineup = lineup
		self.score = 0
		self.outs = 0
		self.batter_up = batter_up
		self.runners = []
		self.lineup.top_of_inning()

	def run_inning(self):
		while(self.outs < 3):
			self.at_bat()

	def at_bat(self):
		player_at_bat = self.lineup.players[self.batter_up]
		outcome = player_at_bat.calculate_outcome()
		if (outcome == Hit.OUT):
			self.outs = self.outs + 1
		else:
			self.runners.append(player_at_bat)
			for runner in self.runners:
				runner.base = runner.base + outcome.value
			self.check_runners()
		self.batter_up = self.batter_up + 1
		if (self.batter_up == len(self.lineup.players)):
			self.batter_up = 0

	def check_runners(self):
		for runner in self.runners:
			if runner.base >= 4:
				self.score = self.score + 1
				runner.base = 0
				self.runners.remove(runner)

class Game:

	def __init__(self, total_innings, lineup):
		self.total_score = 0
		self.total_innings = total_innings
		self.batter_up = 0
		self.lineup = lineup

	def run_game(self):
		for inning_num in range(self.total_innings):
			inning = Inning(self.lineup, self.batter_up)
			inning.run_inning()
			self.total_score = self.total_score + inning.score
			self.batter_up = inning.batter_up