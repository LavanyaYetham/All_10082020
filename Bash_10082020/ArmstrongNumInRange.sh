#!/usr/bin/bash
read -p "Please enter the starting range: " startn
read -p "Please enter the ending range: " endn
for num in `seq $startn $endn`
do
    New=$num
    Len=${#num}
    z=0
    while [ $num -gt 0 ]
    do
        let r=$num%10
        let q=$num/10
        let x=($r**$Len)
        let z=$z+$x
        let num=$q
    done
    if [ $z -eq $New ]
    then
        echo "$New is Armstong Number"
    fi
done
