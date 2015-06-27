#!/bin/bash
i=1
while [ $i -le 3 ]
do
    if [ -f "/media/giliam/Stockage/Programmation/CodingGames/F_HorseRacing/in$i.txt" ]
    then
        python test.py < "in$i.txt" > "out$i.txt"
    else
        break
    fi
    i=$(( $i + 1 ))
done 