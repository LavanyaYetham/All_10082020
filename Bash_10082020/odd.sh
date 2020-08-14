#!/usr/bin/bash
read -p "Please enter the Number : " num
if [ $((num%2)) -ne 0 ]
then
    echo "$num is odd"
else
    echo "$num is not odd number"
fi
