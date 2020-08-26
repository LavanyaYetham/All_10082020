#!/usr/local/bin/python3.8
#Different Ways of Creating Arrays in Numpy
#1.Array()
from numpy import *
arr1=array([1,2,3,4,5])
print (arr1.dtype)
print (arr1)
print ("****************")
arr2=array([1,2,3,4,5.0]) #If One Value is Float all values are Converted into Float
print (arr2.dtype)
print (arr2)
print ("****************")
arr3=array([1,2,3,4,5],float) 
print (arr3.dtype)
print (arr3)
print ("****************")
arr=array([1,2,3,4,5],int) 
print (arr.dtype)
print (arr)

print ("#######################################")
#2.linspace()
#Take three paramters(start,stop,step),stop is also included
arr4=linspace(0,15) #When step is not given Be default 50 Parts
print (arr4)
print ("**************")
arr5=linspace(0,15,4) #Here parts based on Step value
print (arr5)

print ("#######################################")
#3.arange()
arr6=arange(0,15)
print (arr6)
print ("***************")
arr7=arange(0,15,4) #It will Skip Values Based on Step Value
print (arr7)

print ("#######################################")
#4.logspace()
#It wil break the range into parts with Conversion of log values
arr8=logspace(0,15,4)
print (arr8)

print ("#######################################")
#5.zeros()
#It is used When We want create an array of with somesize all Values are by default be Zeros
arr9=zeros(5)
print (arr9.dtype)
print (arr9)
print ("*********")
arr9=zeros(5,int)
print (arr9.dtype)
print (arr9)
print ("#######################################")
#1.ones()
#It is used When We want create an array of with somesize all Values are by default be Ones
arr10=ones(5)
print (arr10.dtype)
print (arr10)
print ("***********")
arr10=ones(5,int)
print (arr10.dtype)
print (arr10)
