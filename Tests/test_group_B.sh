#!/bin/bash
FILE="../script_prono/NSU_prono.py"

for f in $FILE
do
  python3 $f Angleterre Iran
  python3 $f Angleterre Etats_unis
  python3 $f Angleterre Pays_de_galles
  python3 $f Iran Etats_unis
  python3 $f Iran Pays_de_galles
  python3 $f Etats_unis Pays_de_galles
done

exit 0
