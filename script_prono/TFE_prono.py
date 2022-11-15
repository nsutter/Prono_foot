import sys
import random

country_list = [["Allemagne", 11] ,
                ["Angleterre", 5] ,
                ["Arabie_saoudite", 51] ,
                ["Argentine", 3] ,
                ["Australie", 38] ,
                ["Belgique", 2] ,
                ["Bresil", 1] ,
                ["Cameroun", 43] ,
                ["Canada", 41] ,
                ["Croatie", 12] ,
                ["Coree_du_sud", 28] ,
                ["Costa_rica", 31] ,
                ["Danemark", 10] ,
                ["Equateur", 44] ,
                ["Espagne", 7] ,
                ["France", 4] ,
                ["Ghana", 61] ,
                ["Iran", 20] ,
                ["Japon", 24] ,
                ["Maroc", 22] ,
                ["Mexique", 13] ,
                ["Pologne", 26] ,
                ["Pays_bas", 8] ,
                ["Pays_de_galles", 19] ,
                ["Portugal", 9] ,
                ["Qatar", 50] ,
                ["Senegal", 18] ,
                ["Serbie", 21] ,
                ["Suisse", 15] ,
                ["Tunisie", 30] ,
                ["Uruguay", 14] ,
                ["Etats_unis", 16]]

def rotate_score(score1, score2):
    return score2, score1

def get_score(team1, team2):
    team_power1 = 0.0
    team_power2 = 0.0
    score_team1 = 0
    score_team2 = 0
    for country in country_list:
        if( team1 == country[0]):
            team_power1 = (61 - country[1])/100
        if( team2 == country[0]):
            team_power2 = (61 - country[1])/100

    deviation = (team_power1 - team_power2)*5 + 1
    score_team1 = abs(int(random.normalvariate( mu = 1 , sigma = deviation)))
    score_team2 = abs(int(random.normalvariate( mu = 1 , sigma = deviation)))
    if(team_power1 > team_power2):
        if(score_team1 < score_team2):
            score_team1, score_team2 = rotate_score(score_team1,score_team2)
    elif(team_power2 > team_power1):
        if(score_team2 < score_team1):
            score_team1, score_team2 = rotate_score(score_team1,score_team2)

    return score_team1, score_team2

def main():
    score1, score2 = get_score(sys.argv[1], sys.argv[2])
    print( str(score1) + " - " + str(score2) )

if __name__ == "__main__":
    main()
