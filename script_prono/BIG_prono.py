
import sys

cote_Equipe = {"bresil": 4.5,
               "argentine": 6.0,
               "france": 8.0,
               "angleterre": 9.0,
               "espagne": 9.0,
               "allemagne": 11.0,
               "pays_bas": 15.0,
               "belgique": 15.0,
               "portugal": 15.0,
               "danemark": 29.0,
               "croatie": 41.0,
               "uruguay": 41.0,
               "senegal": 81.0,
               "serbie": 81.0,
               "suisse": 81.0,
               "etats_unis": 101.0,
               "mexique": 101.0,
               "pologne": 101.0,
               "pays_de_galles": 151.0,
               "equateur": 151.0,
               "qatar": 251.0,
               "japon": 251.0,
               "maroc": 251.0,
               "ghana": 251.0,
               "cameroun": 251.0,
               "coree_du_sud": 251.0,
               "canada": 251.0,
               "australie": 401.0,
               "tunisie": 401.0,
               "iran": 501.0,
               "costa_rica": 601.0,
               "arabie_saoudite": 601.0}


def extract_cotes(equipes):
  cote_equipe1 = cote_Equipe[equipes[0]]
  cote_equipe2 = cote_Equipe[equipes[1]]

  cotes = (cote_equipe1, cote_equipe2)

  return cotes


def determine_score(cotes):
  if cotes[0] > cotes[1]:
      score = (1, 2)
  else:
      score = (2, 1)
  return score


def format_output(score):
  string_ouput = " - ".join(map(str, score))
  return string_ouput


def result_match():
    if len(sys.argv) == 3:

        equipes = (sys.argv[1].lower(), sys.argv[2].lower())
        cotes = extract_cotes(equipes)
        score = determine_score(cotes)
        resultat = format_output(score)

        print(resultat)
    else:
        print("probleme nombre arguments")


if __name__ == "__main__":
    result_match()

