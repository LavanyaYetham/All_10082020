#!/usr/bin/bash
age=120
if [ "$age" -ge 18 ] || [ "$age" -lt 120 ]
then
    echo "Eligble for Voting"
else
    echo "Not Eligible"
fi

echo "########"
if [ "$age" -ge 18 -o "$age" -lt 120 ]
then
    echo "Eligble for Voting"
else
    echo "Not Eligible"
fi

echo "########"
if [[ "$age" -ge 18 || "$age" -lt 120 ]]
then
    echo "Eligble for Voting"
else
    echo "Not Eligible"
fi


echo "########"
echo "Enter any number"
read n
if [[ ( $n -eq 15 || $n  -eq 45 ) ]]
then
echo "You won the game"
else
echo "You lost the game"
fi
