#!/usr/local/bin/python3.8
"""
For Loop execute the set of statements repeatedly based on the difene Sequence
"""
for i in range(5):
    print (i)
print ("##########")
for j in range(1,5):
    print (j)

print ("##########")
for k in range(1,5,2):
    print (k)
print ("##########")
for k in range(10,1,-2):
    print (k)
print ("*************")
#for loop-Accessing Elements
OS=["Windows","Mac OS","Unix","Linux"]
for x in OS:
    print (x)

print ("*************")
#for loop-seq.of char in string
for i in "Python":
    print (i)
print ("*************")
#for loop-printsquare of numbers
for x in  range(1,11):
    print ("Square of",x,"is",x*x)
print ("*************")
#for loop-print even numbers
print ("Even Numbers between 1 to 25: ")
for x in range(1,26):
    if (x%2 == 0):
        print (x)

print ("*************")
#for loop-print multiplicate table
n=int(input("Enter the number to  display its table : "))
for i in range(1,11):
    print (n,"*",i,"=",n*i)
