#!/bin/bash

RESULT_FILE="Match_score_table.txt"

BIG=0
BBQ=1
DVI=2
FMM=3
JJV=4
LDK=5
NSU=6
OUG=7
PIG=8
TFE=9

SCORE=(0 0 0 0 0 0 0 0 0 0)
CORRECT_WINNER=(0 0 0 0 0 0 0 0 0 0)
CORRECT_SCORE=(0 0 0 0 0 0 0 0 0 0)


for file in Results/*.txt
do
  score_found=0
  match=${file//Results\//}
  match=${match//.txt/}
	
  ## FIND CORRECT SCORE	
  while read line; 
  do 
    arrayline=($line)
    if [ "$match" = "${arrayline[0]}" ];
    then
      total_score=${line//"$match" /}
      score1=${arrayline[1]}; 
      score2=${arrayline[3]}; 
      score_found=1
      
      if [ "$score1" -gt "$score2" ];
      then
        winner=1
      elif [ "$score2" -gt "$score1" ];
	  then
		winner=2
	  else
	    winner=0
	  fi
    fi
  done < $RESULT_FILE
  
  ## COMPUTE RESULT IF SCORE FOUND
  if [ "$score_found" -eq 1 ];
  then
    
    while read line; 
    do
      arrayline=($line)
      score1_prono=${arrayline[0]}
      score2_prono=${arrayline[2]}
      
      if [ ${arrayline[1]} ];
      then
        index_temp=${NAME}
        index=${!index_temp}
      
        if [ "$total_score" = "$line" ];
        then
			((CORRECT_SCORE[$index]+=1))
	    fi
	    
	    if [ "$winner" -eq 1 ];
	    then
	       if [ "$score1_prono" -gt "$score2_prono" ];
	       then
	         ((CORRECT_WINNER[$index]+=1))
	       fi
	    elif [ "$winner" -eq 2 ];
	    then
	      if [ "$score1_prono" -lt "$score2_prono" ];
	      then
	        ((CORRECT_WINNER[$index]+=1))
	      fi
	    else
	      if [ "$score1_prono" -eq "$score2_prono" ];
	      then
	        ((CORRECT_WINNER[$index]+=1))
	      fi
	    fi
      else
	    NAME=${line//\_prono.py/}
	    NAME=${NAME//script\_prono\//}
      fi
    done < $file
  fi
done

j=0
while [ "$j" -lt 10 ]
do
  (( SCORE[$j] =CORRECT_WINNER[$j] * 1 ))
  (( SCORE[$j]+=CORRECT_SCORE[$j] * 2 ))
  (( j+=1 ))
done

echo -e "TOTAL \t WINNER \t SCORE \t TRI" > Point_table.txt
echo -e "${SCORE[0]} \t ${CORRECT_WINNER[0]} \t\t ${CORRECT_SCORE[0]} \t BIG" >> Point_table.txt
echo -e "${SCORE[1]} \t ${CORRECT_WINNER[1]} \t\t ${CORRECT_SCORE[1]} \t BBQ" >> Point_table.txt
echo -e "${SCORE[2]} \t ${CORRECT_WINNER[2]} \t\t ${CORRECT_SCORE[2]} \t DVI" >> Point_table.txt
echo -e "${SCORE[3]} \t ${CORRECT_WINNER[3]} \t\t ${CORRECT_SCORE[3]} \t FMM" >> Point_table.txt
echo -e "${SCORE[4]} \t ${CORRECT_WINNER[4]} \t\t ${CORRECT_SCORE[4]} \t JJV" >> Point_table.txt
echo -e "${SCORE[5]} \t ${CORRECT_WINNER[5]} \t\t ${CORRECT_SCORE[5]} \t LDK" >> Point_table.txt
echo -e "${SCORE[6]} \t ${CORRECT_WINNER[6]} \t\t ${CORRECT_SCORE[6]} \t NSU" >> Point_table.txt
echo -e "${SCORE[7]} \t ${CORRECT_WINNER[7]} \t\t ${CORRECT_SCORE[7]} \t OUG" >> Point_table.txt
echo -e "${SCORE[8]} \t ${CORRECT_WINNER[8]} \t\t ${CORRECT_SCORE[8]} \t PIG" >> Point_table.txt
echo -e "${SCORE[9]} \t ${CORRECT_WINNER[9]} \t\t ${CORRECT_SCORE[9]} \t TFE" >> Point_table.txt
  
sort -k1,1 -n -r -t\t Point_table.txt > Point_table_sorted.txt

rm Point_table.txt
mv Point_table_sorted.txt Point_table.txt
