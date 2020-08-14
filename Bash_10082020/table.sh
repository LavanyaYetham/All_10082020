#!/usr/bin/bash
read -p "Please enter the Number: " num
a=1
while [ $a -lt 10 ]
do
    let b=$num*$a
    echo "$num*$a=$b"
    let a=$a+1
done   
    
