#!/usr/local/bin/python3.6

List1=[]
List1.append(1)
List1.append(2)
List1.append(3)
print (List1)
List1.insert(0,4)
print (List1)
List2=[]
for  i in range(len(List1)):
    for j in range(i+1,len(List1)):
        if List1[i] > List1[j]:
            temp=List1[i]
            List1[i]=List1[j]
            List1[j]=temp
    List2.append(List1[i])
print (List2)

List2.extend(List1)
print (List2)

for i in range(len(List2)):
    for j in range(i+1,len(List2)):
        if List2[i] == List2[j]:
            print (List2[i])

print (List2)
List2.pop()
print (List2)
List2.pop(2)
print (List2)
List2.remove(4)
print (List2)
