import sys
import random

SCORE_MAX = 5

cote_Equipe = { "bresil" : 4.5,
                "argentine" : 6.0,
                "france" : 8.0, 
                "angleterre" : 9.0,
                "espagne" : 9.0,
                "allemagne" : 11.0,
                "pays_bas" : 15.0,
                "belgique" : 15.0,
                "portugal" : 15.0,
                "danemark" : 29.0,
                "croatie" : 41.0,
                "uruguay" : 41.0,
                "senegal" : 81.0,
                "serbie" : 81.0,
                "suisse" : 81.0,
                "etats_unis" : 101.0,
                "mexique" : 101.0,
                "pologne" : 101.0,
                "pays_de_galles" : 151.0,
                "equateur" : 151.0,
                "qatar" : 251.0,
                "japon" : 251.0,
                "maroc" : 251.0,
                "ghana" : 251.0,
                "cameroun" : 251.0,
                "coree_du_sud" : 251.0,
                "canada" : 251.0,
                "australie" : 401.0,
                "tunisie" : 401.0,
                "iran" : 501.0,
                "costa_rica" : 601.0,
                "arabie_saoudite" : 601.0}

score_tab = [ [1.0, 1.3, 1.5, 2.0, 3.0, 5.0, 8.0, 10.0, 1000.0 ] , [0, 1, 1, 1, 1, 1, 2, 2, 3 ] ]

def score (rapport_cote_equipes):
    for i,value in enumerate(score_tab[0]):
        if value > rapport_cote_equipes:
            score = random.randint(min(score_tab[1][i],SCORE_MAX) , min(score_tab[1][i]+1,SCORE_MAX))
            break
    return score

def result_match():
    if len( sys.argv ) == 3:
        cote_equipe1 = cote_Equipe[(sys.argv[1].lower())]
        cote_equipe2 = cote_Equipe[sys.argv[2].lower()]
        rapport_cote_equipes = ( cote_equipe1 / cote_equipe2 )
        score_equipe1 = score(1/rapport_cote_equipes)
        score_equipe2 = score(rapport_cote_equipes)
        resultat = str(score_equipe1) + " - " + str(score_equipe2)
        print (resultat)
    else:
        print ("probleme nombre arguments")

if __name__ == "__main__":
    result_match()
