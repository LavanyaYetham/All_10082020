#!/usr/bin/bash
read -p "Please enter the Starting Range: " startn
read -p "Please enter the Ending Range: " endn
while [ $startn -le $endn ]
do
    if [ $((startn%2)) -eq 0 ]
    then
        echo "$startn is even Number"
    fi
    let startn=$startn+1
done
