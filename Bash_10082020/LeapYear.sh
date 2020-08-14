#!/usr/bin/bash
read -p "Please enter the Number: " Year
if [ $(($Year%4)) -eq 0 ]
then
    if [ $(($Year%100)) -eq 0 ]
    then
        if [ $(($Year%400)) -eq 0 ]
        then
            echo "$Year is Leap Year"
        else
            echo "$Year is not Leap Year"
        fi
    else
        echo "$Year is Leap Year"
    fi
else
    echo "$Year is not Leap Year"
fi
