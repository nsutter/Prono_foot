#!/bin/bash
FILE="../script_prono/NSU_prono.py"

for f in $FILE
do
  python $f Angleterre Iran
  python $f Angleterre Etats_unis
  python $f Angleterre Pays_de_galles
  python $f Iran Etats_unis
  python $f Iran Pays_de_galles
  python $f Etats_unis Pays_de_galles
done

exit 0
