#!/usr/bin/bash
read -p "Please enter the Number: " num
New=$num
z=0
Len=${#num}
while [ $num -gt 0 ]
do
    let r=$num%10
    let q=$num/10
    let x=($r**$Len)
    let z=$z+$x
    let num=$q
done
if [ $New -eq $z ]
then
    echo "$New is Armstrong Number"
else
    echo "$New is not armstrong Number"
fi
