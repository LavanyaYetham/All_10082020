#!/usr/bin/bash
read -p "Please enter the Number: " num
New=$num
z=0
while [ $num -gt 0 ]
do
    let r=$num%10
    let q=$num/10
    let z=($z*10)+$r
    let num=$q
done
echo "Reverse of $New is $z"
