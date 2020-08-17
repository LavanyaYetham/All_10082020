#!/usr/local/bin/python3.8
a1=20
b1=10
#if 
if a1>b1:
    print (a1,"is Geaater than",b1)

print ("##########")
#if else
a2=10
b2=20
if a2>b2:
    print (a2,"is Greater than",b2)
else:
    print (b2,"is Greater than",a2)
print ("###########")
#if elif else
a3=20
b3=20
if a3>b3:
    print (a3,"is Greater than",b3)
elif b3>a3:
    print (b3,"is Greater than",a3)
else:
    print (a3,b3,"are Equal Numbers")

print ("##########")
#Nested if
x=40
y=20
z=30
if x>y:
    if x>z:
        print (x,"is greater than",y,z)
    else:
        print (z,"is greater than",x,y)

