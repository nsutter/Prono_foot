#!/bin/bash
FILE="../script_prono/NSU_prono.py"

for f in $FILE
do
  python3 $f France Australie
  python3 $f France Danemark
  python3 $f France Tunisie
  python3 $f Australie Danemark
  python3 $f Australie Tunisie
  python3 $f Danemark Tunisie
done

exit 0
