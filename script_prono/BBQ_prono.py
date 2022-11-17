from __future__ import division
import sys
from math import *

teams = ["Allemagne", "Angleterre", "Arabie_saoudite", "Argentine", "Australie", "Belgique", "Bresil", "Cameroun", "Canada", "Coree_du_sud", "Costa_rica", "Croatie", "Danemark", "Equateur", "Espagne", "Etats_unis", "France", "Ghana", "Iran", "Japon", "Maroc", "Mexique", "Pays_de_galles", "Pays_bas", "Pologne", "Portugal", "Qatar", "Senegal", "Serbie", "Suisse", "Tunisie", "Uruguay"]
fifa_ranking = [11, 5, 51, 3, 38, 2, 1, 43, 41, 28, 31, 12, 10, 44, 7, 16, 4, 61, 20, 24, 21, 13, 19, 8, 26, 9, 50, 18, 22, 15, 30, 14]
match_played = [55, 62, 60, 56, 40, 60, 59, 54, 46, 63, 60, 59, 60, 49, 58, 66, 61, 46, 46, 66, 70, 77, 52, 52, 54, 57, 68, 68, 53, 57, 66, 52]
nb_victoire_match = [27, 39, 28, 35, 23, 44, 44, 23, 32, 37, 21, 29, 34, 18, 33, 39, 40, 21, 31, 41, 46, 44, 22, 31, 24, 32, 38, 39, 27, 26, 37, 28]
nb_equality_match = [16, 12, 13, 14, 8, 8, 11, 17, 4, 13, 15, 13, 14, 16, 19, 12, 14, 13, 7, 10, 17, 14, 13, 13, 13, 16, 13, 17, 15, 16, 12, 11]
nb_defeat_match = [12, 11, 19, 7, 9, 8, 4, 14, 10, 13, 24, 17, 12, 15, 6, 15, 7, 12, 8, 15, 7, 19, 17, 8, 17, 9, 17, 12, 11, 15, 17, 13]
nb_goals_scored = [125, 140, 77, 106, 78, 155, 128, 61, 125, 97, 59, 98, 116, 64, 128, 125, 126, 58, 94, 138, 131, 121, 60, 116, 93, 117, 116, 99, 120, 105, 96, 78]
nb_goals_received = [66, 44, 58, 42, 29, 50, 22, 43, 31, 53, 68, 78, 45, 56, 46, 50, 52, 38, 25, 54, 41, 71, 52, 47, 63, 46, 72, 45, 58, 61, 53, 45]

 
def calculate_factorial(number):
    indice = 1
    for element in range(2, number + 1):
        indice*=element
    return indice
 
def calculate_poisson_distribution(parameter):
    element = 0 
    proba_team = []
    while element <= 2:
        proba = (e**(-parameter)*parameter**element/calculate_factorial(element)) * 100
        proba_team.append(proba)
        element = element + 1
    proba_goal_team = proba_team.index(max(proba_team)) 
    proba_team.clear()
    return proba_goal_team
 
def calculate_attack_strength(team):
    average_goals_scored = nb_goals_scored[team] / match_played[team]
    average_victoire_match = nb_victoire_match[team] / match_played[team]
    attack_strength = ( average_goals_scored + average_victoire_match )
    return average_goals_scored, attack_strength

def calculate_defense_potential(team):
    average_goals_received = nb_goals_received[team] / match_played[team]
    average_defeat_match = nb_defeat_match[team] / match_played[team]
    defense_potential = ( average_goals_received + average_defeat_match )
    return defense_potential

def calcaulate_average_fifa_ranking(team):
    average_fifa_ranking = ( max(fifa_ranking) - fifa_ranking[team]) / max(fifa_ranking)
    return average_fifa_ranking

def calcaulate_nb_goals_to_be_scored(team_1, team_2):
    function_calculate_attack_strength = calculate_attack_strength(teams.index(team_1))
    average_goals_scored = function_calculate_attack_strength[0]
    attack_strength = function_calculate_attack_strength[1]
    average_fifa_ranking = calcaulate_average_fifa_ranking(teams.index(team_1))
    defense_potential = calculate_defense_potential(teams.index(team_2))
    proba_nb_goals_to_be_scored = average_fifa_ranking * average_goals_scored * attack_strength * defense_potential
    nb_goals_to_be_scored = calculate_poisson_distribution(proba_nb_goals_to_be_scored)
    return nb_goals_to_be_scored

def get_score(team_1, team_2):
    score_team_1 = calcaulate_nb_goals_to_be_scored(team_1, team_2)
    score_team_2 = calcaulate_nb_goals_to_be_scored(team_2, team_1)
    return print( str(score_team_1) + " - " + str(score_team_2) )

def main():
    team_1 = sys.argv[1]
    team_2 = sys.argv[2]  
    get_score(team_1, team_2)


if __name__ == "__main__":
    main()
    