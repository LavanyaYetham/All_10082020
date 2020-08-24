#!/usr/bin/bash
read -p "Enter the Number1: " num1
read -p "Enter the Number2: " num2
if [ $num1 -lt $num2 ]
then
    echo "$num1 is Lower than $num2"
elif [ $num2 -lt $num1 ]
then
    echo "$num2 is Lower than $num1"
else
    echo "$num1 $num2 are equal Number" 
fi

