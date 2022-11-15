#!/bin/bash
FILE="../script_prono/NSU_prono.py"

for f in $FILE
do
  python $f Belgique Canada
  python $f Belgique Maroc
  python $f Belgique Croatie
  python $f Canada Maroc
  python $f Canada Croatie
  python $f Maroc Croatie
done

exit 0
