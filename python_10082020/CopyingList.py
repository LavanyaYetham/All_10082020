#!/usr/local/bin/python3.8
#1.Using slicing technique
List1=[4, 8, 2, 10, 15, 18] 
print ("List1 :",List1)
List1_copy=List1[:]
print ("List1_Copy :",List1_copy)
print ("***************")
def Copy1(L1):
    L1_Copy=L1[:]
    return L1_Copy
L1=[4, 8, 2, 10, 15, 18]
L2=Copy1(L1)
print("Original List:", L1) 
print("Copy List :", L2)
print ("#####################")
#2.Using the extend() method
List2=[4, 8, 2, 10, 15, 18]
print ("List2 :",List2)
List2_copy=[]
List2_copy.extend(List2)
print ("List2_Copy :",List2_copy)
print ("***************")
def Copy2(L3):
    L3_Copy=[]
    L3_Copy.extend(L3)
    return L3_Copy
L3=[1,3,2,4]
L4=Copy2(L3)
print("Original List:", L3) 
print("Copy List :", L4)
print ("#####################")
#3.Using the list() method
List3=[1,2,3,4]
print ("List3 :",List3)
List3_copy=list(List3)
print ("List3_Copy :",List3_copy)
print ("***************")
def Copy3(L5):
    L5_copy=list(L5)
    return L5_copy
L5=[9,8,7]
L6=Copy3(L5)
print("Original List:", L5) 
print("Copy List :", L6)
print ("#####################")
#4.Using the method of Shallow Copy and Deep Copy
import copy
List4=[2,3,4,1]
# using copy for shallow copy
Shallow_Copy=copy.copy(List4)
# using deepcopy for deepcopy   
Deep_Copy=copy.deepcopy(List4)
print (Shallow_Copy)
print (Deep_Copy)
print ("#####################")
#5.Using the append() method
def Copy4(L7):
    L7_copy=[]
    for i in L7:
        L7_copy.append(i)
    return L7_copy
L7=[1,2,4,6]
L8=Copy4(L7)
print("Original List:", L7) 
print("Copy List :", L8)

#6.Using list comprehension
def Cloning(li1): 
    li_copy = [i for i in li1] 
    return li_copy 
li1 = [4, 8, 2, 10, 15, 18] 
li2 = Cloning(li1) 
print("Original List:", li1) 
print("After Cloning:", li2) 




