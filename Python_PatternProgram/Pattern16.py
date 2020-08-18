#!/usr/local/bin/python3.8

for i in range(1,6):
    for j in range(1,i+1):
        print (i,end="")
    print ()

print ("****************")
for i in range(1,6):
    for j in range(5,i-1,-1):
        print (i,end="")
    print ()
print ("****************")
for i in range(5,0,-1):
    for j in range(0,i):
        print (i,end="")
    print ()



"""
OUTPUT:-
# ./Pattern16.py
1
22
333
4444
55555
****************
11111
2222
333
44
5
****************
55555
4444
333
22
1
"""
