#!/bin/bash
FILE="../script_prono/NSU_prono.py"

for f in $FILE
do
  python3 $f Bresil Serbie
  python3 $f Bresil Suisse
  python3 $f Bresil Cameroun
  python3 $f Serbie Suisse
  python3 $f Serbie Croatie
  python3 $f Suisse Cameroun
done

exit 0
