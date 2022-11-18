import sys
import random

TeamRatings = {"bresil": 5,
               "argentine": 5,
               "france": 5,
               "angleterre": 5,
               "espagne": 5,
               "allemagne": 5,
               "pays_bas": 4,
               "belgique": 4,
               "portugal": 4,
               "danemark": 4,
               "croatie": 4,
               "uruguay": 4,
               "senegal": 3,
               "serbie": 3,
               "suisse": 3,
               "etats_unis": 3,
               "mexique": 3,
               "pologne": 3,
               "pays_de_galles": 3,
               "equateur": 3,
               "qatar": 2,
               "japon": 2,
               "maroc": 2,
               "ghana": 2,
               "cameroun": 2,
               "coree_du_sud": 2,
               "canada": 2,
               "australie": 1,
               "tunisie": 1,
               "iran": 1,
               "costa_rica": 1,
               "arabie_saoudite": 1}


def generateScore(teams):

  team1Ratings = TeamRatings[teams[0]]
  team2Ratings = TeamRatings[teams[1]]

  level = abs(team1Ratings - team2Ratings) + 1

  score1 = random.randint(0, level)
  score2 = random.randint(0, level)
  
  if team1Ratings > team2Ratings:
    if score2 > score1:
        output = str(score2) + " - " + str(score1)
    else:
        output = str(score1) + " - " + str(score2)
  elif score1 > score2:
    output = str(score2) + " - " + str(score1)
  else:
    output = str(score1) + " - " + str(score2)   
  
  return output


def result_match():
    if len(sys.argv) == 3:

        teams = (sys.argv[1].lower(), sys.argv[2].lower())
        result = generateScore(teams)

        print(result)
    else:
        print("argument number incorrect")


if __name__ == "__main__":
    result_match()

