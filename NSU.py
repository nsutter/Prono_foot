import sys

score_Allemagne = 1
score_Angleterre = 1
score_Arabie_saoudite = 1
score_Argentine = 1
score_Belgique = 15
score_Bresil = 6
score_Cameroun = 6
score_Canada = 6
score_Croatie = 51
score_Danemark = 31
score_Equatar = 9
score_Espagne = 9
score_France = 7
score_Ghana = 7
score_Japon = 7
score_Maroc = 7
score_Pologne = 7
score_Portugal = 15
score_Coree = 15
score_Iran = 15
score_Pays_Bas = 15
score_Qatar = 51
score_Senegal = 81
score_Serbie = 100
score_Suisse = 150
score_Tunisie = 150
score_Uruguay = 151

def get_country_score(name):
    if(name == "Allemagne"):
        return score_Allemagne
    elif(name == "Angleterre"):
        return score_Angleterre
    elif(name == "Arabie_saoudite"):
        return score_Arabie_saoudite
    elif(name == "Argentine"):
        return score_Argentine
    elif(name == "Belgique"):
        return score_Belgique
    elif(name == "Bresil"):
        return score_Bresil
    elif(name == "Cameroun"):
        return score_Cameroun
    elif(name == "Canada"):
        return score_Canada
    elif(name == "Croatie"):
        return score_Croatie
    elif(name == "Danemark"):
        return score_Danemark
    elif(name == "Equateur"):
        return score_Equatar
    elif(name == "Espagne"):
        return score_Espagne
    elif(name == "France"):
        return score_France
    elif(name == "Ghana"):
        return score_Ghana
    elif(name == "Japon"):
        return score_Japon
    elif(name == "Maroc"):
        return score_Maroc
    elif(name == "Pologne"):
        return score_Pologne
    elif(name == "Portugual"):
        return score_Portugal
    elif(name == "Coree"):
        return score_Coree
    elif(name == "Iran"):
        return score_Iran
    elif(name == "Pays_Bas"):
        return score_Pays_Bas
    elif(name == "Qatar"):
        return score_Qatar
    elif(name == "Senegal"):
        return score_Senegal
    elif(name == "Serbie"):
        return score_Serbie
    elif(name == "Suisse"):
        return score_Suisse
    elif(name == "Tunisie"):
        return score_Tunisie
    elif(name == "Uruguay"):
        return score_Uruguay

def main():
    print( str(get_country_score(sys.argv[1])) + " - " + str(get_country_score(sys.argv[3])) )

if __name__ == "__main__":
    main()
