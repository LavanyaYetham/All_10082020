#!/usr/local/bin/python3.8
#Three Digits and Print all Possible Combinations from the Digits
num1=int(input("Please enter the First Number: "))
num2=int(input("Please enter the Second Number: "))
num3=int(input("Please enter the Third Number: "))
d=[]
d.append(num1)
d.append(num2)
d.append(num3)
for i in range(0,3):
    for j in range(0,3):
        for k in range(0,3):
            if (i!=j&j!=k&k!=i):
                print (d[i],d[j],d[k])
#Two Digits and Print all Possible Combinations from the Digits
num1=int(input("Enter first number: "))
num2=int(input("Enter second number:"))
List=[]
List.append(num1)
List.append(num2)
for l in range(0,2):
    for m in range(0,2):
        if (l!=m&m!=l):
            print (List[l],List[m])
