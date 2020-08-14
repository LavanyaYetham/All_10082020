#!/usr/bin/bash
read -p "Please enter the starting Range: " startn
read -p "Please enter the ending Range: " endn
while [ $startn -le $endn ]
do
    if [ $((startn%2)) -ne 0 ]
    then
        echo "$startn is Odd Number"
    fi
    let startn=$startn+1
done
