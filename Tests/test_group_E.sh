#!/bin/bash
FILE="../script_prono/NSU_prono.py"

for f in $FILE
do
  python3 $f Espagne Costa_rica
  python3 $f Espagne Allemagne
  python3 $f Espagne Japon
  python3 $f Costa_rica Allemagne
  python3 $f Costa_rica Japon
  python3 $f Allemagne Japon
done

exit 0
