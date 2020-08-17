#!/usr/bin/bash
age=120
if [ "$age" -ge 18 ] && [ "$age" -lt 120 ]
then
    echo "Eligble for Voting"
else
    echo "Not Eligible"
fi

echo "########"
if [ "$age" -ge 18 -a "$age" -lt 120 ]
then
    echo "Eligble for Voting"
else
    echo "Not Eligible"
fi

echo "########"
if [[ "$age" -ge 18 && "$age" -lt 120 ]]
then
    echo "Eligble for Voting"
else
    echo "Not Eligible"
fi
