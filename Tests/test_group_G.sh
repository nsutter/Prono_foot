#!/bin/bash
FILE="../script_prono/NSU_prono.py"

for f in $FILE
do
  python $f Bresil Serbie
  python $f Bresil Suisse
  python $f Bresil Cameroun
  python $f Serbie Suisse
  python $f Serbie Croatie
  python $f Suisse Cameroun
done

exit 0
