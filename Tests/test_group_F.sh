#!/bin/bash
FILE="../script_prono/NSU_prono.py"

for f in $FILE
do
  python3 $f Belgique Canada
  python3 $f Belgique Maroc
  python3 $f Belgique Croatie
  python3 $f Canada Maroc
  python3 $f Canada Croatie
  python3 $f Maroc Croatie
done

exit 0
