#!/bin/bash
FILE="../script_prono/NSU_prono.py"

for f in $FILE
do
  python $f France Australie
  python $f France Danemark
  python $f France Tunisie
  python $f Australie Danemark
  python $f Australie Tunisie
  python $f Danemark Tunisie
done

exit 0
