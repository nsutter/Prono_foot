import numpy as np
from datetime import date
import sys

teams = ["Allemagne", "Angleterre", "Arabie_saoudite", "Argentine", "Australie", "Belgique", "Bresil", "Cameroun", "Canada", "Coree_du_sud", "Costa_rica", "Croatie", "Danemark", "Equateur", "Espagne", "Etats_unis", "France", "Ghana", "Iran", "Japon", "Maroc", "Mexique", "Pays_de_galles", "Pays_bas", "Pologne", "Portugal", "Qatar", "Senegal", "Serbie", "Suisse", "Tunisie", "Uruguay"]
fifa_score = [650, 728, 437, 773, 488, 816, 841, 471, 475, 530, 503, 645, 666, 464, 715, 627, 759, 393, 564, 559, 563, 644, 569, 694, 548, 676, 439, 584, 563, 635, 507, 638]
fifa_trend = [-8, -9, 2, 3, 5, -5, 3, -13, 1, 4, 3, 13, 1, 1, -1, -7, -5, -1, 6, 4, 5, -4, -12, 15, 2, -2, -2, 0, 14, 14, 0, -2]
win_probability = [7.21, 8.03, 0.00, 6.45, 0.01, 7.90, 15.73, 0.00, 0.01, 0.35, 0.00, 2.31, 2.03, 0.17, 11.53, 0.46, 17.93, 0.02, 0.60, 0.48, 0.01, 1.37, 0.41, 7.70, 0.82, 5.11, 0.35, 0.19, 0.24, 1.00, 0.01, 1.48]

group_probability = np.zeros((32, 4), dtype=int)
group_probability[teams.index("Allemagne")] = [41, 39, 15, 5]
group_probability[teams.index("Angleterre")] = [63, 23, 10, 4]
group_probability[teams.index("Arabie_saoudite")] = [3, 10, 25, 62]
group_probability[teams.index("Argentine")] = [69, 21, 8, 2]
group_probability[teams.index("Australie")] = [5, 15, 36, 44]
group_probability[teams.index("Belgique")] = [55, 27, 13, 5]
group_probability[teams.index("Bresil")] = [68, 21, 8, 3]
group_probability[teams.index("Cameroun")] = [5, 15, 27, 53]
group_probability[teams.index("Canada")] = [8, 18, 32, 42]
group_probability[teams.index("Coree_du_sud")] = [9, 20, 33, 38]
group_probability[teams.index("Costa_rica")] = [2, 8, 27, 63]
group_probability[teams.index("Croatie")] = [27, 36, 23, 14]
group_probability[teams.index("Danemark")] = [28, 44, 20, 8]
group_probability[teams.index("Equateur")] = [15, 27, 31, 27]
group_probability[teams.index("Espagne")] = [51, 34, 12, 3]
group_probability[teams.index("Etats_unis")] = [17, 30, 29, 24]
group_probability[teams.index("France")] = [62, 26, 9, 3]
group_probability[teams.index("Ghana")] = [8, 18, 32, 42]
group_probability[teams.index("Iran")] = [7, 19, 29, 45]
group_probability[teams.index("Japon")] = [7, 18, 46, 29]
group_probability[teams.index("Maroc")] = [10, 20, 32, 38]
group_probability[teams.index("Mexique")] = [14, 33, 34, 19]
group_probability[teams.index("Pays_de_galles")] = [14, 28, 31, 27]
group_probability[teams.index("Pays_bas")] = [59, 24, 12, 5]
group_probability[teams.index("Pologne")] = [14, 35, 34, 17]
group_probability[teams.index("Portugal")] = [56, 27, 12, 5]
group_probability[teams.index("Qatar")] = [7, 18, 29, 46]
group_probability[teams.index("Senegal")] = [18, 31, 29, 22]
group_probability[teams.index("Serbie")] = [13, 30, 33, 24]
group_probability[teams.index("Suisse")] = [15, 34, 31, 20]
group_probability[teams.index("Tunisie")] = [5, 15, 35, 45]
group_probability[teams.index("Uruguay")] = [27, 36, 23, 14]

team_strength = np.zeros((32, 3), dtype=int)
team_strength[teams.index("Allemagne")] = [84, 85, 83]
team_strength[teams.index("Angleterre")] = [86, 83, 83]
team_strength[teams.index("Arabie_saoudite")] = [71, 72, 72]
team_strength[teams.index("Argentine")] = [85, 83, 83]
team_strength[teams.index("Australie")] = [72, 72, 71]
team_strength[teams.index("Belgique")] = [82, 83, 81]
team_strength[teams.index("Bresil")] = [85, 85, 83]
team_strength[teams.index("Cameroun")] = [75, 75, 73]
team_strength[teams.index("Canada")] = [75, 78, 72]
team_strength[teams.index("Coree_du_sud")] = [78, 73, 75]
team_strength[teams.index("Costa_rica")] = [77, 73, 73]
team_strength[teams.index("Croatie")] = [83, 82, 78]
team_strength[teams.index("Danemark")] = [78, 83, 80]
team_strength[teams.index("Equateur")] = [74, 76, 75]
team_strength[teams.index("Espagne")] = [84, 85, 84]
team_strength[teams.index("Etats_unis")] = [77, 78, 76]
team_strength[teams.index("France")] = [86, 84, 83]
team_strength[teams.index("Ghana")] = [75, 76, 74]
team_strength[teams.index("Iran")] = [81, 72, 72]
team_strength[teams.index("Japon")] = [75, 78, 76]
team_strength[teams.index("Maroc")] = [76, 74, 78]
team_strength[teams.index("Mexique")] = [79, 77, 76]
team_strength[teams.index("Pays_de_galles")] = [78, 76, 77]
team_strength[teams.index("Pays_bas")] = [83, 83, 83]
team_strength[teams.index("Pologne")] = [80, 76, 76]
team_strength[teams.index("Portugal")] = [83, 85, 84]
team_strength[teams.index("Qatar")] = [73, 71, 71]
team_strength[teams.index("Senegal")] = [79, 77, 77]
team_strength[teams.index("Serbie")] = [80, 80, 75]
team_strength[teams.index("Suisse")] = [77, 78, 78]
team_strength[teams.index("Tunisie")] = [72, 75, 72]
team_strength[teams.index("Uruguay")] = [82, 81, 80]

score_probability = np.zeros((32, 32), dtype=np.dtype([('f1', np.int16), ('f2', np.int16)]))
score_probability.fill((1, 1))
score_probability[teams.index("Angleterre"), teams.index("Pays_bas")] = (1, 3)
score_probability[teams.index("Pays_bas"), teams.index("Angleterre")] = (3, 1)

score_probability[teams.index("Argentine"), teams.index("Danemark")] = (2, 1)
score_probability[teams.index("Danemark"), teams.index("Argentine")] = (1, 2)

score_probability[teams.index("Argentine"), teams.index("Pays_bas")] = (1, 0)
score_probability[teams.index("Pays_bas"), teams.index("Argentine")] = (0, 1)

score_probability[teams.index("Argentine"), teams.index("France")] = (1, 0)
score_probability[teams.index("France"), teams.index("Argentine")] = (0, 1)

score_probability[teams.index("Argentine"), teams.index("Bresil")] = (1, 0)
score_probability[teams.index("Bresil"), teams.index("Argentine")] = (0, 1)

score_probability[teams.index("Etats_unis"), teams.index("Senegal")] = (2, 1)
score_probability[teams.index("Senegal"), teams.index("Etats_unis")] = (1, 2)

score_probability[teams.index("Etats_unis"), teams.index("France")] = (0, 1)
score_probability[teams.index("France"), teams.index("Etats_unis")] = (1, 0)

score_probability[teams.index("Pologne"), teams.index("France")] = (1, 2)
score_probability[teams.index("France"), teams.index("Pologne")] = (2, 1)

score_probability[teams.index("Allemagne"), teams.index("Belgique")] = (2, 1)
score_probability[teams.index("Belgique"), teams.index("Allemagne")] = (1, 2)

score_probability[teams.index("Allemagne"), teams.index("Bresil")] = (0, 3)
score_probability[teams.index("Bresil"), teams.index("Allemagne")] = (3, 0)

score_probability[teams.index("Coree_du_sud"), teams.index("Bresil")] = (0, 3)
score_probability[teams.index("Bresil"), teams.index("Coree_du_sud")] = (3, 0)

score_probability[teams.index("Portugal"), teams.index("Bresil")] = (0, 0)
score_probability[teams.index("Bresil"), teams.index("Portugal")] = (0, 0)

score_probability[teams.index("Croatie"), teams.index("Espagne")] = (2, 1)
score_probability[teams.index("Espagne"), teams.index("Croatie")] = (1, 2)

score_probability[teams.index("Croatie"), teams.index("Portugal")] = (0, 1)
score_probability[teams.index("Portugal"), teams.index("Croatie")] = (1, 0)

score_probability[teams.index("Suisse"), teams.index("Portugal")] = (0, 2)
score_probability[teams.index("Portugal"), teams.index("Suisse")] = (2, 0)

score_probability[teams.index("France"), teams.index("Portugal")] = (4, 2)
score_probability[teams.index("Portugal"), teams.index("France")] = (2, 4)


def atk_factor(team):
    fifa_factor = (fifa_score[team] + (fifa_trend[team] * 5)) / 10
    strength_factor = (team_strength[team][0] + team_strength[team][1]) * 100 / 200
    return fifa_factor + strength_factor

def def_factor(team):
    fifa_factor = (fifa_score[team] + (fifa_trend[team] * 10)) / 10
    strength_factor = (team_strength[team][1] + team_strength[team][2]) * 100 / 200
    return fifa_factor + strength_factor

def compute_score(team_1, team_2):
    initial_score = score_probability[team_1, team_2].copy()
    atk_factor_team_1 = atk_factor(team_1)
    def_factor_team_1 = def_factor(team_1)
    atk_factor_team_2 = atk_factor(team_2)
    def_factor_team_2 = def_factor(team_2)

    qualification_team_1 = group_probability[team_1][0] + group_probability[team_1][1]
    qualification_team_2 = group_probability[team_2][0] + group_probability[team_2][1]

    current_date = date.today()
    finals_date = date(2022, 12, 3)

    if ( finals_date > current_date ):
        if ( (qualification_team_1 - qualification_team_2) > 10 ):
            atk_factor_team_1 += 5
            def_factor_team_1 += 5
        elif ( (qualification_team_2 - qualification_team_1) > 10 ):
            atk_factor_team_2 += 5
            def_factor_team_2 += 5

    initial_score[0] = initial_score[0] + ((atk_factor_team_1 - def_factor_team_2) // 20)
    initial_score[1] = initial_score[1] + ((atk_factor_team_2 - def_factor_team_1) // 20)

    if ( (score_probability[team_1, team_2][0] != 1 and score_probability[team_1, team_2][1] != 1)
        or (score_probability[team_1, team_2][0] == 1 and score_probability[team_1, team_2][1] != 1)
        or (score_probability[team_1, team_2][0] != 1 and score_probability[team_1, team_2][1] == 1) ):
        initial_score[0] = (initial_score[0] + score_probability[team_1, team_2][0]) // 2
        initial_score[1] = (initial_score[1] + score_probability[team_1, team_2][1]) // 2

    if ( finals_date <= current_date and initial_score[0] == initial_score[1] ):
        if ( win_probability[team_1] > win_probability[team_2] ):
            initial_score[0] += 1
        else:
            initial_score[1] += 1
    
    initial_score[0] = min(max(initial_score[0], 0), 4)
    initial_score[1] = min(max(initial_score[1], 0), 4)
    print(str(initial_score[0]) + " - " + str(initial_score[1]))

# matches = [(a, b) for idx, a in enumerate(teams) for b in teams[idx + 1:]]
# for match in matches:
#     print(match)
#     compute_score(teams.index(match[0]), teams.index(match[1]))


def main():
    team_1 = sys.argv[1]
    team_2 = sys.argv[2]

    compute_score(teams.index(team_1), teams.index(team_2))

if __name__ == "__main__":
    main()
