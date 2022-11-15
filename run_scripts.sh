#!/bin/bash

#############################################
#                VARIABLES                  #
#############################################

Countries=("Allemagne" "Angleterre" "Arabie_saoudite" "Argentine" "Belgique" "Bresil" "Cameroun" "Canada" "Croatie" "Danemark" "Equateur" "Espagne" "France" "Ghana" "Japon" "Maroc" "Pologne" "Portugual" "Coree" "Iran" "Pays_Bas" "Qatar" "Senegal" "Serbie" "Suisse" "Tunisie" "Uruguay")
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
