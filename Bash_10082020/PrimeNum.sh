#!/usr/bin/bash
read -p "please enter the number: " num
n=2
while [ $n -lt $num ]
do
    if [ $(($num%$n)) -eq 0 ]
    then
        echo "$num is not Prime"
        x=0
        break
    else
        x=1
    fi
    let n=$n+1
done
if [ $x -eq 1 ]
then
    echo "$num is  Prime"
fi

