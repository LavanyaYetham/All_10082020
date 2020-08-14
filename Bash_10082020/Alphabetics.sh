#!/usr/bin/bash
count=1
for a in {a..z}
do
    echo "$a:$count"
    let count=$count+1
done
