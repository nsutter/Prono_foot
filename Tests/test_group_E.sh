#!/bin/bash
FILE="../script_prono/NSU_prono.py"

for f in $FILE
do
  python $f Espagne Costa_rica
  python $f Espagne Allemagne
  python $f Espagne Japon
  python $f Costa_rica Allemagne
  python $f Costa_rica Japon
  python $f Allemagne Japon
done

exit 0
