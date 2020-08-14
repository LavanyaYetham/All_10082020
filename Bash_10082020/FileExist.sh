#!/usr/bin/bash
read -p "Enter the Filename: " fname
if [ -f $fname ]
then
    echo "$fname is Existed"
else
    echo "$fname is not existed"
fi
#When File is not existed then crete  a file Using Below Code
echo "**********"

read -p "Enter the Filename: " name
if [ -f $name ]
then
    echo "$name is Existed"
else
    echo "$name is not existed"
    read -p "Do You want to create File y/n ?: " object
    if [ $object == "y" ]
    then
        echo "$name file is Creating...."
        touch $name
        sleep 3
        echo "$name file is Created"
    fi
fi
