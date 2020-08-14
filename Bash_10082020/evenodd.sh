#!/usr/bin/bash
read -p "Please enter the Number: " num
if [ $((num%2)) -eq 0 ]
then
    echo "$num is even number"
elif [ $((num%2)) -ne 0 ]
then
    echo "$num is odd Number"
fi
