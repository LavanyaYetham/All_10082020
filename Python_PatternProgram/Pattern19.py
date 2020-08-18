#!/usr/local/bin/python3.8
for i in range(65,70):
    for j in range(65,i+1):
        print (chr(j),end="")
    print ()
print ("*********************")
for i in range(5,0,-1):
    for j in range(0,i):
        print (chr(j+65),end="")
    print ()
print ("*********************")
for i in range(0,5):
    for j in range(4,i-1,-1):
        print (chr(j+65),end="")
    print ()


"""
OUTPUT:-
# ./Pattern19.py
A
AB
ABC
ABCD
ABCDE
*********************
ABCDE
ABCD
ABC
AB
A
*********************
EDCBA
EDCB
EDC
ED
E
"""
