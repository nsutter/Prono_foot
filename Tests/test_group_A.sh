#!/bin/bash
FILE="../script_prono/NSU_prono.py"

for f in $FILE
do
  python $f Qatar Equateur
  python $f Qatar Senegal
  python $f Qatar Pays_bas
  python $f Equateur Senegal
  python $f Equateur Pays_bas
  python $f Senegal Pays_bas
done

exit 0
