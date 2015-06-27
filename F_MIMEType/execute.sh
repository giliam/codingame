#!/bin/bash
i=1
while [ $i -le 5 ]
do
    if [ -f "/media/giliam/Stockage/Programmation/CodingGames/MIMEType/in$i.txt" ]
    then
        python test.py < "in$i.txt" > "out$i.txt"
    else
        break
    fi
    i=$(( $i + 1 ))
done 