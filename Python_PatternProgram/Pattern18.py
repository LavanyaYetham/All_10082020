#!/usr/local/bin/python3.8
for i in range(65,70):
    for j in range(65,i+1):
        print (chr(i),end="")
    print ()
print ("*********************")
for i in range(0,5):
    for j in range(4,i-1,-1):
        print (chr(i+65),end="")
    print ()

print ("*********************")
for i in range(5,0,-1):
    for j in range(0,i):
        print (chr(i+64),end="")
    print ()

"""
OUTPUT:-
# ./Pattern18.py
A
BB
CCC
DDDD
EEEEE
*********************
AAAAA
BBBB
CCC
DD
E
*********************
EEEEE
DDDD
CCC
BB
A
"""
