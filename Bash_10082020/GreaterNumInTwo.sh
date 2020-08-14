#!/usr/bin/bash
read -p "Please enter the number1: " num1
read -p "Please enter the number2: " num2
if [ $num1 -gt $num2 ]
then
    echo "$num1 is Greater than $num2"
elif [ $num2 -gt $num1 ]
then
    echo "$num2 is Greater then $num1"
else
    echo "$num1 $num2 are Equal Numbers"
fi
