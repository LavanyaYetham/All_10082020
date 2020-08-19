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

echo "########"
echo "Enter username: "
read username
echo "Enter password: "
read password
if [[ ( $username == "admin" && $password == "secret" ) ]]; then
echo "valid user"
else
echo "invalid user"
fi
