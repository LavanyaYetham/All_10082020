#!/usr/local/bin/python3.8

for i in range(1,6):
    for j in range(1,6):
        if j == 1 or j == 5 or i==j:
            print ("*",end="")
        else:
            print (" ",end="")
    print ()
