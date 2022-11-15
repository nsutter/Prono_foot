import sys
import numpy as np
import random

teams = ["Allemagne", "Angleterre", "Arabie_saoudite", "Argentine", "Australie", "Belgique", "Bresil", "Cameroun", "Canada", "Coree_du_sud", "Costa_rica", "Croatie", "Danemark", "Equateur", "Espagne", "Etats_unis", "France", "Ghana", "Iran", "Japon", "Maroc", "Mexique", "Pays_de_galles", "Pays_bas", "Pologne", "Portugal", "Qatar", "Senegal", "Serbie", "Suisse", "Tunisie", "Uruguay"]
cote = [11, 9, 601, 6, 350, 15, 5, 251, 252, 251, 601, 41, 29, 151, 9, 101, 7, 251, 501, 251, 251, 100, 151, 15, 101, 15, 251, 81, 81, 70, 401, 41]

big_diff = 1.1
small_diff = 0.5

def avoid_equity(winning_team, score1, score2):
    if( score1 == score2 and winning_team != 0 ):
        if( win == 1 ):
            if( score2 > 0 ):
                score2 -= 1
            else:
                score1 += 1
        else:
            if( score1 > 0 ):
                score1 -= 1
            else:
                score2 += 1

    return score1, score2

def compute_score(index_team_1, index_team_2):

    cote_diff = cote[index_team_1] - cote[index_team_2]
    mu_team1 = 1.32
    mu_team2 = 1.32
    sigma = 0.6

    if(cote_diff < 0):
        win = 1
        if(cote_diff < -200):
            mu_team1 += big_diff
            mu_team2 -= big_diff
        elif(cote_diff < -20):
            mu_team1 += small_diff
            mu_team2 -= small_diff
        elif(cote[index_team_1] < 40):
            mu_team2 -= 1
            sigma = 0.4

    elif(cote_diff > 0):
        win = 2
        if(cote_diff > 200):
            mu_team2 += big_diff
            mu_team1 -= big_diff
        elif(cote_diff > 20):
            mu_team2 += small_diff
            mu_team1 -= small_diff
        elif(cote[index_team_2] < 40):
            mu_team1 -= 1
            sigma = 0.4
    else:
        win = 0
        mu_team1 = 2
        mu_team2 = 2
        sigma = 0.2

    score1 = abs( round( random.gauss(mu_team1, sigma=sigma) ) )
    score2 = abs( round( random.gauss(mu_team2, sigma=sigma) ) )

    # score1, score2 = avoid_equity(win, score1, score2)

    print( str(score1) + " - " + str(score2) )

def main():
    team_1 = sys.argv[1]
    team_2 = sys.argv[2]
    compute_score(teams.index(team_1), teams.index(team_2))

if __name__ == "__main__":
    main()
