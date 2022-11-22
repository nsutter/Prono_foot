import os
import sys
import random

teams = { "Qatar" : 4,
          "Equateur" : 5,
          "Senegal" : 6,
          "Pays_bas" : 7,
          "Angleterre" : 8,
          "Iran" : 3,
          "Etats_unis" : 6,
          "Pays_de_galles" : 6,
          "Argentine" : 9,
          "Arabie_saoudite" : 2,
          "Mexique" : 5,
          "Pologne" : 7,
          "France" : 11,
          "Australie" : 6,
          "Danemark" : 8,
          "Tunisie" :4,
          "Espagne" : 9,
          "Costa_rica" : 3,
          "Allemagne" : 10,
          "Japon" : 5,
          "Belgique" :9,
          "Canada" : 3,
          "Maroc" : 3,
          "Croatie" : 6,
          "Bresil" : 12,
          "Serbie" : 6,
          "Suisse" : 8,
          "Cameroun" : 4,
          "Portugal" : 10,
          "Ghana" : 4,
          "Uruguay" : 7,
          "Coree_du_sud" :5 ,       
        }
eval_E1 = teams[sys.argv[1]]
eval_E2 = teams[sys.argv[2]]
prono = eval_E1 - eval_E2

if prono > 5: 
    score_E1 = 3
    score_E2 = 0
elif prono > 0: 
    score_E1 = 2
    score_E2 = 1
elif prono < -5: 
    score_E1 = 0
    score_E2 = 3
elif prono < 0: 
    score_E1 = 1
    score_E2 = 2
elif prono == 0:
	score_E1 = 1
	score_E2 = 1

proba = random.randint(1,10)
if proba == 3:
    score_E2 = score_E1
elif proba == 4 or proba == 5:
    score_E1 += 1
elif proba == 6 or proba == 7:
    score_E2 += 1
elif proba == 8:
    score_E1 += 2
elif proba == 9:
    score_E2 += 2
elif proba == 10:
    score_E1 = 0
    score_E2 = 0
    
print( str(score_E1) + " - " + str(score_E2) )
