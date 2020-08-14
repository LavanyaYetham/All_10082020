#!/usr/bin/bash
read -p "Enter the Filename/Directory : " name
if [ -e $name ]
then
    if [ -f $name ]
    then
        echo "$name is Existed and It is a File"
    elif [ -d $name ]
    then
        echo "$name is Existed and It is Directory"
    fi
else
    echo "$name is not existed"
fi
#When File is not existed then crete  a file Using Below Code
echo "**********"

read -p "Enter the Filename/Directory : " name
if [ -e $name ]
then
    if [ -f $name ]
    then
        echo "$name is Existed and It is a File"
    elif [ -d $name ]
    then
        echo "$name is Existed and It is Directory"
    fi
else
    echo "$name is not existed"
    read -p "Do You Want to Create File/Dir?: " Object
    if [ $Object ==  "File" ]
    then
        touch $name
        echo "$name File is Creating...."
        sleep 3
        echo "$name File is Created"
    elif [ $Object ==  "Dir" ]
    then
        mkdir $name
        echo "$name Directory is Creating...."
        sleep 3
        echo "$name Directory is Created"
    fi
fi
