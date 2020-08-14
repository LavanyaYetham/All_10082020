#!/usr/bin/bash
read -p "Please enter the starting range: " startn
read -p "Please enter the ending range: " endn
for num in `seq $startn $endn`
do
    n=2
    while [ $n -lt $num ]
    do
        if [ $(($num%$n)) -ne 0 ]
        then
            echo "$num is  Prime"
            x=0
            break
        else
            x=1
            break
        fi
    let n=$n+1
    done
done
    
