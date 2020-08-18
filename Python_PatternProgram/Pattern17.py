#!/usr/local/bin/python3.8

for i in range(1,6):
    for j in range(1,i+1):
        print (j,end="")
    print ()
print ("****************")
for i in range(6,1,-1):
    for j in range(1,i):
        print (j,end="")
    print ()

print ("****************")
for i in range(1,6):
    for j in range(5,i-1,-1):
        print (j,end="")
    print ()



"""
OUTPUT:-
]# ./Pattern17.py
1
12
123
1234
12345
****************
12345
1234
123
12
1
****************
54321
5432
543
54
5
"""
