#!/usr/bin/bash
read -p "Enter the Directory Name: " fname
if [ -d $fname ]
then
    echo "$fname is Existed"
else
    echo "$fname is not existed"
fi
#When Directory is not existed then create  a Directory Using Below Code
echo "**********"

read -p "Enter the Directory Name: " name
if [ -d $name ]
then
    echo "$name is Existed"
else
    echo "$name is not existed"
    read -p "Do You want to create Directory y/n ?: " object
    if [ $object == "y" ]
    then
        echo "$name Directory is Creating...."
        mkdir $name
        sleep 3
        echo "$name Directory is Created"
    fi
fi
