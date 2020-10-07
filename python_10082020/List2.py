#!/usr/bin/python

List=[1,2,3,4,5,2,4,3]
print List
print List[2]
print List[:]
print List[:3]
print List[1:]
print List[0:3]

print "Duplicate Values from List are: "
for i in range(len(List)):
    for j in range(i+1,len(List)):
        if List[i] == List[j]:
            print List[i]

print "Sorting the List"
print "List Before sorting:",
print List
x=[]
for i in range(len(List)):
    for j in range(i+1,len(List)):
        if List[i] > List[j]:
            temp=List[i]
            List[i]=List[j]
            List[j]=temp
    x.append(List[i])

print "List After Sorting:",
print x
print "List before Starting: "
a=[1,2,3,4,5,2,4,3]
print a
a.sort()
print "List After Sorting:"
print a
