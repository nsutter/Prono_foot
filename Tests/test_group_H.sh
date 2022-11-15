#!/bin/bash
FILE="../script_prono/NSU_prono.py"

for f in $FILE
do
  python $f Portugal Ghana
  python $f Portugal Uruguay
  python $f Portugal Coree_du_sud
  python $f Ghana Uruguay
  python $f Ghana Coree_du_sud
  python $f Uruguay Coree_du_sud
done

exit 0
