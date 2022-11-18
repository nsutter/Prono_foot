#!/usr/bin/env python3
# coding: utf-8

__author__ = "David Leval"
__version__ = "1.0"

""" Football Mondial Prono (DVI) """

import sys
import random

stats = {
   "Allemagne" : 7.21, 
   "Angleterre" : 8.03,
   "Arabie_saoudite" : 0.0,
   "Argentine" : 6.45,
   "Australie" : 0.01,
   "Belgique" : 7.90,
   "Bresil" : 15.73,
   "Cameroun" : 0.0,
   "Canada" : 0.01,
   "Coree_du_sud" : 0.35,
   "Costa_rica" : 0.0,
   "Croatie" : 2.31,
   "Danemark" : 2.03,
   "Equateur" : 0.17,
   "Espagne" : 11.53,
   "Etats_unis" : 0.46,
   "France" : 17.93,
   "Ghana" : 0.02,
   "Iran" : 0.60,
   "Japon" : 0.48,
   "Maroc" : 0.01,
   "Mexique" : 1.37,
   "Pays_de_galles" : 0.41,
   "Pays_bas" : 7.70,
   "Pologne" : 0.82,
   "Portugal" : 5.11,
   "Qatar" : 0.35,
   "Senegal" : 0.19,
   "Serbie" : 0.24,
   "Suisse" : 1.00,
   "Tunisie" : 0.01,
   "Uruguay" : 1.48
}

def rdm_score_with_weights(weights):
   return random.choices(list(range(5)), weights=weights, k=1)[0]

def winner_rdm_score():
   return rdm_score_with_weights(weights=(10, 20, 50, 30, 10))

def loser_rdm_score():
   return rdm_score_with_weights(weights=(50, 40, 10, 5, 1))

def get_prono(team_1, team_2):
   stats_team_match = dict((k, stats[k]) for k in [team_1, team_2] if k in stats)
   winner = max(stats_team_match, key= stats_team_match.get)
   prono = dict()
   if winner == team_1:
      prono["score_1"] = winner_rdm_score()
      prono["score_2"] = loser_rdm_score()
   else:
      prono["score_1"] = loser_rdm_score()
      prono["score_2"] = winner_rdm_score()
   return prono

if __name__ == "__main__":
   prono = get_prono(sys.argv[1], sys.argv[2])
   print( "{} - {}".format(prono["score_1"], prono["score_2"]) )