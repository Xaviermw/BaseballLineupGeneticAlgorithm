import components.lineup as lu
from components.players import TatersPlayer
import yaml
from genetic_logic.genetic_generation import GeneticGeneration, FitMetric

FIT_METRIC = FitMetric.WIN_PERCENTAGE
player_parameters = yaml.load(open('player_parameters.yaml'), Loader=yaml.FullLoader)
genetic_parameters = yaml.load(open('genetic_parameters.yaml'), Loader=yaml.FullLoader)

def print_lineup_and_stats(lineup):
	lineup.print_lineup()
	print("Win Percentage: " + str(lineup.record.win_percentage()))
	print("Average Score: " + str(lineup.average_score()))

def final_printout(parents):
	print()
	print()
	print("Final Most Fit")
	print() 
	[print_lineup_and_stats(lineup) for lineup in parents]

parents = [lu.create_fully_random_lineup(player_parameters['players_in_lineup'], player_parameters['double_percentage'], player_parameters['hr_percentage'], player_parameters['walk_percentage'], player_parameters['triple_percentage']) for i in range(genetic_parameters['starting_lineups'])]

for generation in range(genetic_parameters['total_generations']):
	genetic_generation = GeneticGeneration(parents, genetic_parameters['mutations'], player_parameters['players_in_lineup'], player_parameters['double_percentage'], player_parameters['hr_percentage'], player_parameters['walk_percentage'], player_parameters['triple_percentage'], genetic_parameters['innings_in_game'], genetic_parameters['seasons_to_play'], generation+1, FIT_METRIC)
	genetic_generation.create_mutants()
	genetic_generation.create_children()
	genetic_generation.simulate_lineup_scores()
	genetic_generation.calculate_most_fit_lineups()
	genetic_generation.print_generation_most_fit()
	parents = genetic_generation.best_lineups

final_printout(parents)
