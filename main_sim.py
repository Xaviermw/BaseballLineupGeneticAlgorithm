import components.lineup as lu
from genetic_logic.genetic_round import GeneticRound, FitMetric

PLAYERS_IN_LINEUP = 9
INNINGS_IN_GAME = 9
HR_PERCENTAGE = 0.085
TRIPLE_PERCENTAGE = 2.0/15
DOUBLE_PERCENTAGE = 0.215
WALK_PERCENTAGE = 0.375
STARTING_LINEUPS = 20
SEASONS_PLAYED = 10
TOTAL_GENERATIONS = 100
MUTATIONS = 4
FIT_METRIC = FitMetric.WIN_PERCENTAGE

def print_lineup_and_stats(lineup):
	print("Lineup: " + str(lineup.players))
	print("Win Percentage: " + str(lineup.record.win_percentage()))
	print("Average Score: " + str(lineup.average_score()))

def final_printout(parents):
	print()
	print()
	print("Final Most Fit")
	print() 
	[print_lineup_and_stats(lineup) for lineup in parents]


parents = [lu.create_fully_random_lineup(PLAYERS_IN_LINEUP, DOUBLE_PERCENTAGE, HR_PERCENTAGE, WALK_PERCENTAGE, TRIPLE_PERCENTAGE) for i in range(STARTING_LINEUPS)]

for generation in range(TOTAL_GENERATIONS):
	genetic_round = GeneticRound(parents, MUTATIONS, PLAYERS_IN_LINEUP, DOUBLE_PERCENTAGE, HR_PERCENTAGE, WALK_PERCENTAGE, TRIPLE_PERCENTAGE, INNINGS_IN_GAME, SEASONS_PLAYED, FIT_METRIC)
	genetic_round.create_mutants()
	genetic_round.create_children()
	genetic_round.simulate_lineup_scores()
	genetic_round.calculate_most_fit_lineup()
	parents = genetic_round.best_lineups

final_printout(parents)
