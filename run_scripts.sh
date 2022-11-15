#!/bin/bash

#############################################
#                VARIABLES                  #
#############################################

Countries=("Allemagne" "Angleterre" "Arabie_saoudite" "Argentine" "Australie" "Belgique" "Bresil" "Cameroun" "Canada" "Coree_du_sud" "Costa_rica" "Croatie" "Danemark" "Equateur" "Espagne" "Etats_unis" "France" "Ghana" "Iran" "Japon" "Maroc" "Mexique" "Pays_de_galles" "Pays_bas" "Pologne" "Portugal", "Qatar" "Senegal" "Serbie" "Suisse" "Tunisie" "Uruguay")
error=0

#############################################
#           ASK AND CHECK COUNTRIES         #
#############################################
read -p "Enter first country: " FirstCountry
for Country in "${Countries[@]}"
do
  if [ "$Country" = "$FirstCountry" ];
  then
    error=1
  fi
done

if [ $error -eq 0 ];
then
  echo "Error wrong country name"
  exit 1
else
  error=0
fi

read -p "Enter second country: " SecoundCountry
for Country in "${Countries[@]}"
do
  if [ "$Country" = "$SecoundCountry" ];
  then
    error=1
  fi
done

for element in "${array[@]}"
do
   if [ "$element" = "SecoundCountry" ];
   then
      error=1
   fi
done

if [ $error -eq 0 ];
then
  echo "Error wrong country name"
  exit 1
fi


if [ "$FirstCountry" = "$SecoundCountry" ];
then
  echo "twice same country"
  exit 1
fi

#############################################
#     RUN ALL SCRIPTS AND COLLECT DATA      #
#############################################

FILE="Results/$FirstCountry-$SecoundCountry.txt"

if test -f $FILE; then
  rm $FILE
fi

for f in script_prono/*.py
do
  echo "Processing $f"
  echo "$f" >> $FILE
  python $f $FirstCountry $SecoundCountry >> $FILE
done

exit 0
