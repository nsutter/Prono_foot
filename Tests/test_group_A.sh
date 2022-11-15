#!/bin/bash
FILE="../script_prono/NSU_prono.py"

for f in $FILE
do
  python3 $f Qatar Equateur
  python3 $f Qatar Senegal
  python3 $f Qatar Pays_bas
  python3 $f Equateur Senegal
  python3 $f Equateur Pays_bas
  python3 $f Senegal Pays_bas
done

exit 0
