#!/usr/local/bin/python3.8
#To Find Dupicate Items from Array
a=[1,2,4,5,2,1]
print ("Original Array :",a)
L=[]
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i] == a[j]:
            L.append(a[i])

print ("Duplicate items from array: ",L)


arr = [2,3,1];     
for i in range(0,len(arr)):
    for j in range(i+1,len(arr)):
        if (arr[i] > arr[j]):
            arr[i],arr[j]=arr[j],arr[i]

for i in range(0,len(arr)):
    print (arr[i])    
