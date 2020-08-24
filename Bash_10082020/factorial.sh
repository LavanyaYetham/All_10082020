#!/usr/bin/bash
read -p "Enter the Number: " num
a=$num
while [ $num -gt 1 ]
do
    let b=$num-1
    let a=$a*$b
    let num=$b
done
echo $a


