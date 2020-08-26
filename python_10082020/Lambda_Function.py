#!/usr/local/bin/python3.8
#To findout the even numbers from list using lambda(filter)
#filter function is used to select some particular elements from a sequence(like lists, sets, tuples, etc) of elements.
List1=[1,2,3,4,5,6]
Evens=list(filter(lambda n:n%2==0,List1))
print (Evens)
print ("******************")
Nums=filter(lambda x:x>3,List1)
print (list(Nums))
#the map function is used to apply a particular operation to every element in a sequence
List2=[1,2,3,4,5,6]
Odds=list(filter(lambda n:n%2!=0,List2))
Doubles=list(map(lambda n:n*2,Odds))
print (Odds)
print (Doubles)
print ("******************")
#reduce()
from functools import reduce
List3=[9,8,7,6,5,4]
Evens=list(filter(lambda n:n%2==0,List3))
Sum=reduce(lambda a,b:a+b,Evens)
print (Evens)
print (Sum)

