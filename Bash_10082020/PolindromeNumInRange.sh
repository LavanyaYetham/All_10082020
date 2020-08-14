#!/usr/bin/bash
read -p "Please enter the starting range: " startn
read -p "Please enter the ending range: " endn
for num in `seq $startn $endn`
do
    New=$num
    z=0
    while [ $num -gt 0 ]
    do
        let r=$num%10
        let q=$num/10
        let z=($z*10)+r
        let num=$q
    done
    if [ $z -eq $New ]
    then
        echo "$New is Polindrome Number"
    fi
done

