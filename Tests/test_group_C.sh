#!/bin/bash
FILE="../script_prono/NSU_prono.py"

for f in $FILE
do
  python $f Argentine Arabie_saoudite
  python $f Argentine Mexique
  python $f Argentine Pologne
  python $f Arabie_saoudite Mexique
  python $f Arabie_saoudite Pologne
  python $f Mexique Pologne
done

exit 0
