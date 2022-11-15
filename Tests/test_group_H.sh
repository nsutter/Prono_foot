#!/bin/bash
FILE="../script_prono/NSU_prono.py"

for f in $FILE
do
  python3 $f Portugal Ghana
  python3 $f Portugal Uruguay
  python3 $f Portugal Coree_du_sud
  python3 $f Ghana Uruguay
  python3 $f Ghana Coree_du_sud
  python3 $f Uruguay Coree_du_sud
done

exit 0
