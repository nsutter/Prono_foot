# Prono_foot #

Ce dépôt est un dépôt de Paris sur la coupe du monde de foot 2022 entre plusieurs personnes. Les scores étant pariés par des scripts écrits par chacune des personnes. 

## Contenu ##

Dans le dossier results se trouve les pari de tous les script, un fichier par match. 
Dans le dossier test de trouve des tests pour pouvoir lancer chaque poule sur un script, tous les tests peuvent être lancés avec run_all_tests.sh. 
Enfin le dossier scripts contient l'ensemble des programmes pour prendre les paris, un programme par joueur. 

Le script run_scripts.sh permet de lancer pour un match tous les scripts des joueurs.  

## Règles ##

Le but du jeu est de faire un programme python permettant de faire un pari
pour chaque match de la coupe du monde. Le programme doit donner pour chaque
math un score.

Le programme:
* doit être écrit en **python**
* ne doit pas écrire de fichier sur la machine à par lui-même (mise à jour OTA)
* peut utiliser la connexion réseau
* doit sortir un résultat avec un temps d'éxecution de moins de 3 min
* respecter le format de sortie
* sera exécuté une fois pour chaque match, un jour avant celui-ci


**En de non respect aucun point ne sera attribué.**

## Interface d'entrée ##

Le programme devrait être un programme python nommé `<trigramme>_prono.py`
, pour NSU cela donne par exemple: `NSU_prono.py`.

Le programme sera exécuté avec la commande suivante: `python <trigramme>_prono.py <pays1> <pays2>`.

> Le pays1 et pays2 sera parmis l'un des suivants (les deux étant différent):
> * Allemagne
> * Angleterre
> * Arabie_saoudite
> * Argentine
> * Australie
> * Belgique
> * Bresil
> * Cameroun
> * Canada
> * Coree_du_sud
> * Costa_rica
> * Croatie
> * Danemark
> * Equateur
> * Etats_unis
> * Espagne
> * France
> * Ghana
> * Iran
> * Japon
> * Maroc
> * Mexique
> * Pologne
> * Portugal
> * Pays_bas
> * Pays_de_galles
> * Qatar
> * Senegal
> * Serbie
> * Suisse
> * Tunisie
> * Uruguay

## Interface de sortie ##

Le programme doit sortie un résultat dans la sortie strandard au format texte.
Il devra être formaté de la manière suivante: `<score pays1> - <score pays2>`. Ce qui donne par exemple: `2 - 0`.

 Le score doit être un entier **entre 0 et 9**.

 ## Calcul des points ##

**Seul le score final du match compte**. En cas de tirs au but le score avant la
 session de tirs au but sera pris.
