#!/usr/local/bin/python3.8
for i in range(1,6):
    for j in range(1,i+1):
        print ("*",end="")
    print ()
print ("#############")
for i in range(1,6):
    for j in range(6,i,-1):
        print ("*",end="")
    print ()
