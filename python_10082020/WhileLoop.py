#!/usr/local/bin/python3.8
"""
while loop execute the statements as long as the condition is True
"""
i=1            #Initialization
while i<=3:    #Condition
    print ("Yes")
    i=i+1      #Increament/Decreament
print ("********************")
#while inside while

i=1
while i<=3:
    print ("Hello",end=" ")
    j=1
    while j<=4:
        print ("World",end=" ")
        j=j+1
    i=i+1
    print ()
print ("********************")
n=0
while n!=1:
    print ("You are inside the while loop: ")
    print ("Press 1 to exit from the loop: ")
    n=int(input())
print ("You are out of the while loop")
