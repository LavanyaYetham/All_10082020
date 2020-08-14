#!/usr/local/bin/python3.8
for i in range(0,4):
    for j in range(0,4):
        print ("#",end="")
    print ()

print ("@@@@@@@@@@@@")
for i in range(0,5):
    for j in range(i):
        print ("#",end="")
    print ()
print ("@@@@@@@@@@@@")
for i in range(5,0,-1):
    for j in range(i-1):
        print ("#",end="")
    print ()
