#!/usr/local/bin/python3.8
a=5
b=6
print ("Before Swap ")
print ('a: ',a)
print ('b: ',b)
temp=a
a=b
b=temp
print ("After Swap ")
print ('a: ',a)
print ('b: ',b)
#Swap Case Without Using Third Variable
print ("##############")
a=5
b=6
print ("Before Swap ")
print ('a: ',a)
print ('b: ',b)
a=a+b
b=a-b
a=a-b
print ("After Swap ")
print ('a: ',a)
print ('b: ',b)
#So,that We are Using XOR(^)
print ("##############")
a=5
b=6
print ("Before Swap ")
print ('a: ',a)
print ('b: ',b)
a=a^b
b=a^b
a=a^b
print ("After Swap ")
print ('a: ',a)
print ('b: ',b)
#Another Way
print ("##############")
a=5
b=6
print ("Before Swap ")
print ('a: ',a)
print ('b: ',b)
a,b=b,a
print ("After Swap ")
print ('a: ',a)
print ('b: ',b)
