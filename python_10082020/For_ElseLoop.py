#!/usr/local/bin/python3.8

#1.
L1=[10,16,20,25,18]
for num in L1:
    if num%5==0:
        print (num)
print ("*************")
#2.
L2=[10,16,20,25,18]
for num in L2:
    if num%5==0:
        print (num)
        break
print ("*************")
#3.
L3=[12,16,18,21,26]
for num in L3:
    if num%5==0:
        print (num)
        break
    else:
        print ("Not Found")
print ("*************")
#4.
L4=[12,16,18,21,26]
for num in L4:
    if num%5==0:
        print (num)
        break
else:
    print ("Not Found")
print ("*************")
#5.
L5=[10,16,20,25,18]
for num in L5:
    if num%5==0:
        print (num)
else:
    print ("Not Found")
print ("*************")
#6.
L6=[10,16,20,25,18]
for num in L6:
    if num%5==0:
        print (num)
        break
else:
    print ("Not Found")
