#!/usr/bin/bash
read -p "Please enter the numer : " num
if [ $((num%2)) -eq 0 ]
then
    echo "$num is even number"
else
    echo "$num is not even number"
fi
