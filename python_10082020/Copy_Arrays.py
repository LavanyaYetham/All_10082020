#!/usr/local/bin/python3.8
from numpy import *
arr1=array([1,2,3,4,5])
arr2=arr1+5
print (arr2)
print ("##########################")
arr3=array([1,2,3,4,5])
print (sin(arr3))
print ("##########################")
#Aliasing:- When the two different arrays having same address is called "Aliasing"
arr4=array([1,2,3])
arr5=arr4
print (arr4)
print (id(arr4))
print (arr5)
print (id(arr5))

