#!/bin/bash
FILE="../script_prono/NSU_prono.py"

for f in $FILE
do
  python3 $f Argentine Arabie_saoudite
  python3 $f Argentine Mexique
  python3 $f Argentine Pologne
  python3 $f Arabie_saoudite Mexique
  python3 $f Arabie_saoudite Pologne
  python3 $f Mexique Pologne
done

exit 0
