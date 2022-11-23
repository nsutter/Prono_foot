import sys
import random

cote_team1 = 0.0
cote_team2 = 0.0 
score_team1 = 0
score_team2 = 0

cote_winamax = [["bresil", 4.50] ,
                ["argentine", 6.50] ,
                ["france", 8.0] ,
                ["espagne", 10] ,
                ["angleterre", 11] ,
                ["allemagne", 13] ,
                ["pays_bas", 14] ,
                ["portugal", 18] ,
                ["belgique", 20] ,
                ["danemark", 35] ,
                ["uruguay", 50] ,
                ["croatie", 60] ,
                ["serbie", 125] ,
                ["suisse", 125] ,
                ["senegal", 125] ,
                ["mexique", 200] ,
                ["etats_unis", 250],
                ["pologne", 250] ,
                ["equateur", 300] ,
                ["australie", 400] ,
                ["japon", 400] ,
                ["maroc", 350] ,
                ["pays_de_galles", 400] ,
                ["iran", 500] ,
                ["coree_du_sud", 500] ,
                ["cameroun", 600] ,
                ["ghana", 600] ,
                ["canada", 700] ,
                ["qatar", 750] ,
                ["costa_rica", 1000] ,
                ["arabie_saoudite", 1000] ,
                ["tunisie", 1000]]


def get_score(cote_team1,cote_team2):
    
    cote_diff = abs(cote_team1 - cote_team2)

    if cote_diff < 25.0 :
        score_team1 = 1
        score_team2 = 1
    elif  25.0 <= cote_diff < 100.0 : 
        score_team1 = 1
        score_team2 = 2    
    elif  100.0 <= cote_diff < 200.0 : 
        score_team1 = 0
        score_team2 = 1
    elif  200.0 <= cote_diff < 300.0 : 
        score_team1 = 1
        score_team2 = 2
    elif  300.0 <= cote_diff < 400.0 : 
        score_team1 = 0
        score_team2 = 2
    elif cote_diff >= 400.0 :
        score_team1 = 0
        score_team2 = 3

    return score_team1, score_team2

def compute_score(team1, team2):

    for country in cote_winamax:
        if( team1 == country[0]):
            cote_team1 = country[1]
        if( team2 == country[0]):
            cote_team2 = country[1]
    
    score_team1, score_team2 = get_score(cote_team1,cote_team2)

    if cote_team1 - cote_team2 > 0 : 
            return score_team1, score_team2
    elif cote_team1 - cote_team2 < 0 :  
        return score_team2, score_team1
    elif cote_team1 == cote_team2 :
        return 2,1


def main():
    score1, score2 = compute_score(sys.argv[1].lower(), sys.argv[2].lower())
    print( str(score1) + " - " + str(score2) )

if __name__ == "__main__":
    main()